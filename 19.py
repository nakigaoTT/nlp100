# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    file_name = nlp.get('hightemp_py.txt')

    with open(file_name, 'r') as f:
        data = [l[:-1].split(' ')[0] for l in f]

    sorted_data = sorted(set(data), key=lambda x: data.count(x), reverse=True)

    for line in sorted_data:
        print(line)

    #UNIX
    nlp.unix("cut -d ' ' -f 1 %s | sort | uniq -c | sort -nr -k1" % file_name)
