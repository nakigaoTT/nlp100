# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第3章: 正規表現

Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．

28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．

@author t-take
"""

import json
import re
import nlp


if __name__ == '__main__':

    json_file = nlp.get('jawiki-country_uk.json')
    with open(json_file, 'r') as f:
        jdata = json.load(f)

    pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$',
                         re.MULTILINE + re.DOTALL)
    base_info = pattern.findall(jdata['text'])[0]

    # 強調マークアップの除去
    pattern = re.compile(r"\'{2,5}", re.MULTILINE + re.DOTALL)
    base_info = pattern.sub('', base_info)

    # 二重括弧内情報（内部リンク，ファイル，カテゴリ，リダイレクト）の除去 [[xxx]]
    pattern = re.compile(r'\[\[(.*?)\]\]', re.MULTILINE + re.DOTALL)
    base_info = pattern.sub(
        lambda x: (x.group().replace('[[', '').replace(']]', '')
                   ).split('|')[0].split(':')[-1].split('#')[0], base_info)

    # リダイレクト表示 #REDIRECT の削除
    pattern = re.compile(r'#REDIRECT ', re.MULTILINE + re.DOTALL)
    base_info = pattern.sub('', base_info)

    # 外部リンクの削除
    pattern = re.compile(r'\[.*?\]', re.MULTILINE + re.DOTALL)
    base_info = re.sub(r'\[.*?\]', '', base_info)

    # スタブの除去
    pattern = re.compile(r'\{\{(.*?)\}\}', re.MULTILINE + re.DOTALL)
    base_info = pattern.sub(
        lambda x: x.group().replace('{{', '').replace('}}', '').split('|')[-1],
        base_info)

    # コメントアウトの除去
    pattern = re.compile(r'<!-- .*? -->', re.MULTILINE + re.DOTALL)
    base_info = pattern.sub('', base_info)

    # <bf>, <ref>の除去
    pattern = re.compile(r'<\/?[br|ref][^>]*?>', re.MULTILINE + re.DOTALL)
    base_info = pattern.sub('', base_info)

    # 辞書構築
    info = {}
    for parts in filter(lambda x: x != '', base_info.split('\n|')):
        parts = parts.split(' = ')
        info.update({parts[0]: parts[1]})

    for key, value in info.items():
        print('%s:: %s' % (key, value))
