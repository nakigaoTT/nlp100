# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    inf = nlp.get('hightemp_py.txt')
    out1 = nlp.output('col1.txt')
    out2 = nlp.output('col2.txt')

    with open(inf, 'r') as rf, open(out1, 'w') as wf1, open(out2, 'w') as wf2:
        for line in rf:
            line = line.split(' ')
            wf1.write(line[0] + '\n')
            wf2.write(line[1] + '\n')

    # UNIX
    nlp.unix("cut -d ' ' -f 1 < %s" % inf)
    nlp.unix("cut -d ' ' -f 2 < %s" % inf)
