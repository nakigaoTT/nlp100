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

29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

@author t-take
"""

import json
import re
import urllib
import urllib.request
import urllib.parse
import nlp


def get_base_info(jdata):
    """基礎情報の取得"""
    # 基礎情報部分の取得
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

    return info


if __name__ == '__main__':

    json_file = nlp.get('jawiki-country_uk.json')
    with open(json_file, 'r') as f:
        jdata = json.load(f)

    info = get_base_info(jdata)

    # リクエスト生成
    url = ('https://commons.wikimedia.org/w/api.php?'
           + 'action=query'
           + '&format=json'
           + '&titles=File:' + urllib.parse.quote_plus(info['国旗画像'])
           + '&prop=imageinfo'
           + '&iiprop=url')
    with urllib.request.urlopen(url) as response:
        html = response.read()
    data = json.loads(html.decode('utf-8'))

    # URL取り出し
    url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    print(url)
