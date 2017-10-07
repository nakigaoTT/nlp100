# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

@author t-take
"""


if __name__ == '__main__':

    import nlp
    from collections import Counter
    import matplotlib.pyplot as plt

    mecab_file = nlp.get('neko.txt.mecab')
    parser = nlp.parse_sentence(mecab_file)

    neko_counter = Counter([char['surface'] for sen in parser for char in sen])
    counts = list(zip(*neko_counter.most_common()))[1]

    plt.figure()
    plt.plot(range(1, 401), counts[:400])
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Zipf's low")
    plt.xlabel('rank of occuration')
    plt.ylabel('Frequencys')
    plt.gca().tick_params(axis='both', direction='in')
    plt.show()
