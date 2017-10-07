# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

@author t-take
"""


if __name__ == '__main__':

    import nlp
    from collections import Counter

    mecab_file = nlp.get('neko.txt.mecab')
    parser = nlp.parse_sentence(mecab_file)

    neko_counter = Counter([char['surface'] for sen in parser for char in sen])

    print('rank: (char, freq)')
    for rank, contents in enumerate(neko_counter.most_common()[:20]):
        print('%4d:' % (rank + 1), contents)
