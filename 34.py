# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．

@author t-take
"""


if __name__ == '__main__':

    import nlp

    mecab_file = nlp.get('neko.txt.mecab')

    parser = nlp.parse_sentence(mecab_file)

    target = set()
    for sentence in parser:
        before = []
        for char in sentence:
            if len(before) < 2:
                before.append(char)
                continue
            if (before[0]['pos'] == '名詞' and before[1]['surface'] == 'の'
                and char['pos'] == '名詞'):
                target.add(before[0]['surface'] + before[1]['surface']
                           + char['surface'])
            before = [before[1], char]

    print(target)
