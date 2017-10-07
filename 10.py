# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第2章: UNIXコマンドの基礎

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で
格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして
実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．

@author t-take
"""


if __name__ == '__main__':

    file_name = 'hightemp.txt'

    with open(file_name, 'r') as f:
        num_colmn = f.read().count('\n')

    print('colmn number is %d.' % num_colmn)

    # UNIXコマンド実行結果
    import nlp
    nlp.unix('wc hightemp.txt')
