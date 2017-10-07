# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

@author t-take
"""

import nlp


if __name__ == '__main__':

    file_name = nlp.get('hightemp_py.txt')

    with open(file_name, 'r') as f:
        data = sorted([l[:-1].split(' ') for l in f], key=lambda x: x[2])

    for d in data:
        print(d)

    #UNIX
    nlp.unix('sort -k 3,3 %s' % file_name)
