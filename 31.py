# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

31. 動詞
動詞の表層形をすべて抽出せよ．

@author t-take
"""


if __name__ == '__main__':

    import nlp

    mecab_file = nlp.get('neko.txt.mecab')

    parser = nlp.parse_sentence(mecab_file)
    surfaces = set(morpheme['surface'] for sen in parser for morpheme in sen)
    print(surfaces)
