# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

CaboCha:
    https://blog.spot-corp.com/other/2016/07/19/cabocha_nlp.html

40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），
品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果
（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，
3文目の形態素列を表示せよ．

@author t-take
"""

import CaboCha
import nlp


class Morph(object):
    """形態素表現"""
    def __init__(self, cabocha):
        super(Morph, self).__init__()

        self.cabocha = cabocha

        # 形態素
        self.surface, feature = self.cabocha.split('\t')
        feature = feature.split(',')
        self.base = feature[6]
        self.pos = feature[0]
        self.pos1 = feature[1]

    def __repr__(self):
        return '「{}」({}/{})'.format(self.surface, self.pos, self.pos1)


def morph_sentence(cabocha_file):
    """係り受け解析された.cabochaファイルから１文ずつクラス化する"""
    morpheme_list = []
    f = open(cabocha_file, 'r')

    for line in f:
        # End of sentence
        if line[:3] == 'EOS':
            # print(morpheme_list)
            if morpheme_list:
                yield morpheme_list
                morpheme_list = []
            else:
                continue

        # 要素抽出
        if '\t' not in line or ',' not in line:
            continue
        morpheme = Morph(line)  # 形態素設定
        if morpheme.pos1 != '空白':
            morpheme_list.append(morpheme)

    else:
        f.close()
        raise StopIteration


if __name__ == '__main__':

    file_name = nlp.get('neko.txt')
    file_name_parsed = nlp.output('neko.txt.cabocha')

    # 係り受け解析
    with open(file_name, 'r') as rf, open(file_name_parsed, 'w') as wf:
        parser = CaboCha.Parser()
        for line in rf:
            wf.write(parser.parse(line).toString(CaboCha.FORMAT_LATTICE))

    with open(file_name_parsed, 'r') as f:
        for i, line in enumerate(f):
            print(line)
            if i > 10:
                break

    # 形態素抽出
    morph_iter = morph_sentence(file_name_parsed)
    for i, morph_list in enumerate(morph_iter):
        if i == 3:
            for morph in morph_list:
                print(morph)
