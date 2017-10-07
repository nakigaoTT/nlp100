# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．

@author t-take
"""

import sys
import nlp


if __name__ == '__main__':

    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 3

    file_name = nlp.get('hightemp.txt')

    with open(file_name, 'r') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line, end='')

    # UNIX
    nlp.unix('head -n %d %s' % (n, file_name))
