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

25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．

@author t-take
"""

import json
import re
import nlp


if __name__ == '__main__':

    json_file = nlp.get('jawiki-country_uk.json')
    with open(json_file, 'r') as f:
        jdata = json.load(f)

    pattern = re.compile(r'''^\{\{基礎情報.*?$(.*?)^\}\}$''',
                         re.MULTILINE + re.DOTALL)
    base_info = pattern.findall(jdata['text'])[0]

    info = {}
    for parts in filter(lambda x: x != '', base_info.split('\n|')):
        parts = parts.split(' = ')
        info.update({parts[0]: parts[1]})

    for key, value in info.items():
        print('%s:: %s' % (key, value))
