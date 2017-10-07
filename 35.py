# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

@author t-take
"""


if __name__ == '__main__':

    import nlp

    mecab_file = nlp.get('neko.txt.mecab')
    parser = nlp.parse_sentence(mecab_file)

    juncture = set()
    nouns_series = []
    for sentence in parser:
        for char in sentence:
            if char['pos'] == '名詞':
                nouns_series.append(char['surface'])
            else:
                if len(nouns_series) > 1:
                    juncture.add(''.join(nouns_series))
                nouns_series = []
        if len(nouns_series) > 1:
            juncture.add(''.join(nouns_series))
        nouns_series = []

    print(juncture)
