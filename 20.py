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

20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

@author t-take
"""

import gzip
import json

import nlp


if __name__ == '__main__':

    wikipedia_file = nlp.get('jawiki-country.json.gz')
    out_json_file = nlp.output('jawiki-country_uk.json')

    with gzip.open(wikipedia_file, 'rt', 'utf_8') as gf:
        for line in gf:
            jdata = json.loads(line)
            if jdata['title'] == u'イギリス':
                print(jdata['text'])
                break

    with open(out_json_file, 'w') as wf:
        json.dump(jdata, wf, indent=4)
