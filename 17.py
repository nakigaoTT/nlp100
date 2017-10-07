# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    file_name = nlp.get('col1.txt')

    with open(file_name, 'r') as f:
        name_kind = set([l[:-1] for l in f if l])   # ''と`\n`を除外

    print(name_kind)

    # UNIX
    nlp.unix('sort %s | uniq' % file_name)
