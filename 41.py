# -*- coding: utf-8 -*-
"""
Create on Tue Oct 03 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト
（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を
メンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．

@author t-take
"""

import nlp
from nlp import Morph


class Chunk(object):
    """分節表現"""
    def __init__(self, dependency=None, morph_list=[]):
        super(Chunk, self).__init__()
        self.morphs = []
        self.dst = -1
        self.srcs = []

        if dependency is not None:
            dependency = dependency.split(' ')

            if not (len(dependency) == 5
                    and dependency[0] == '*' and dependency[2][-1] == 'D'):
                raise ValueError(
                    'dependency `%s` is invalide format' % dependency)

            self.num = int(dependency[1])       # 分節番号
            self.dst = int(dependency[2][:-1])  # 係り先の分節番号（係り先なし: -1）
            _num = dependency[3].split('/')
            self.head_num = int(_num[0])        # 主辞の形態素番号
            self.machine_num = int(_num[1])     # 機械語の形態素番号
            self.score = float(dependency[4])   # かかり関係のスコア

        if morph_list:
            for morpheme in morph_list:
                self.morphs.append(Morph(morpheme))

    def __repr__(self):
        return '[{}]{} {}'.format(
            self.num, ''.join(map(str, self.morphs)),
            '-> [%d]' % self.dst if self.dst != -1 else '-.')


def sen2chunk(sentence):
    """１文から分節を表すクラスChunkのリストを生成する．"""
    chunks = []
    morph_list = []

    dependency = sentence[0].replace('\n', '')

    for line in sentence[1:]:

        if line[0] == '*':  # `*`から始まる行は係り受け情報を示す．
            chunks.append(Chunk(dependency, morph_list))
            dependency = line.replace('\n', '')
            morph_list = []

        else:               # それ以外は形態素を表す
            morph_list.append(line)

    else:
        chunks.append(Chunk(dependency, morph_list))

    # 最後にかかり元を追加する
    for chunk in chunks:
        dst = chunk.dst
        if dst != -1:
            if chunks[dst].num == dst:
                chunks[dst].srcs.append(chunk.num)

    return chunks


def make_chunk(cabocha_file):
    """１文ごとのChunkオブジェクトのリストを作成する"""
    sentence = []
    f = open(cabocha_file, 'r')

    for line in f:

        if line[:3] == 'EOS':
            if sentence:
                yield sen2chunk(sentence)
                sentence = []
            else:
                continue

        else:   # lineが'EOS'でないときのみ追加
            sentence.append(line)

    else:   # close the file at finish the loop
        f.close()
        raise StopIteration


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    cabocha = make_chunk(cabocha_file)

    for i, chunks in enumerate(cabocha):
        if i + 1 == 8:
            for chunk in chunks:
                print(chunk)
            break
