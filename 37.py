# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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
    rank10 = neko_counter.most_common()[:10]

    x, y = zip(*rank10)

    mpl.rcParams['font.family'] = 'Osaka'
    plt.figure()
    plt.bar(range(1, 11), y, tick_label=x)
    plt.title('出現頻度上位10語')
    plt.ylabel('出現回数')
    plt.gca().tick_params(axis='both', direction='in')
    plt.show()
