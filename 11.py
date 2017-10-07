# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
もしくはexpandコマンドを用いよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    in_file_name = nlp.get('hightemp.txt')
    out_file_name_py = nlp.output('hightemp_py.txt')
    out_file_name_unix = nlp.output('hightemp_unix.txt')

    with open(in_file_name, 'r') as rf, open(out_file_name_py, 'w') as wf:
        for line in rf:
            wf.write(line.replace('\t', ' '))

    # UNIXコマンド
    nlp.unix("sed -e 's/\t/ /g' %s > %s" % (in_file_name, out_file_name_unix),
             notice=False)
    # nlp.unix("tr '\t' ' ' < %s > %s" % (in_file_name, out_file_name_unix),
    #          notice=False)
    # nlp.unix("expand -t 1 < %s > %s" % (in_file_name, out_file_name_unix),
    #          notice=False)
