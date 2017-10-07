# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

38. ヒストグラム
単語の出現頻度のヒストグラム
（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

@author t-take
"""


if __name__ == '__main__':

    import nlp
    from collections import Counter
    import matplotlib.pyplot as plt
    import matplotlib as mpl

    mecab_file = nlp.get('neko.txt.mecab')
    parser = nlp.parse_sentence(mecab_file)

    neko_counter = Counter([char['surface'] for sen in parser for char in sen])
    counts = list(zip(*neko_counter.most_common()))[1]

    plt.figure()
    plt.hist(counts, bins=50, range=(0, 400))
    plt.xlim((0, 400))
    plt.ylim((0, 200))
    plt.title('The histgram of occuration')
    plt.ylabel('Frequencys')
    plt.gca().tick_params(axis='both', direction='in')
    plt.show()
