# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．

@author t-take
"""

import sys
import nlp


if __name__ == '__main__':

    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 5

    in_file_name = nlp.get('hightemp.txt')
    out_file_name = nlp.output('row%d.txt')

    with open(in_file_name, 'r') as rf:
        text = rf.read().split('\n')

    for i, line in enumerate(text):
        with open(out_file_name % (i // n + 1), 'a') as wf:
            wf.write(line + '\n')

    # UNIX
    nlp.unix('split -l %d %s' % (n, in_file_name))
