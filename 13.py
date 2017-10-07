# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べた
テキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    in1 = nlp.get('col1.txt')
    in2 = nlp.get('col2.txt')
    outf = nlp.output('col1+2.txt')

    with open(in1, 'r') as rf1, open(in2, 'r') as rf2, open(outf, 'w') as wf:
        for col1, col2 in zip(rf1, rf2):
            wf.write(','.join([col1.replace('\n', ''), col2]))

    # UNIX
    nlp.unix("paste -d ',' %s %s" % (in1, in2))
