# -*- coding: utf-8 -*-
"""
Create on Tue Oct 10 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．
    - 各文節は（表層形の）形態素列で表現する
    - パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．
```
    吾輩は -> 見た
    ここで -> 始めて -> 人間という -> ものを -> 見た
    人間という -> ものを -> 見た
    ものを -> 見た
```

@author t-take
"""
from __future__ import division, absolute_import, print_function

from itertools import islice
import nlp


def make_tree(sentence, chunk):
    if chunk.dst > 0:
        return ' -> '.join([chunk.surface('norm'),
                            make_tree(sentence, sentence[chunk.dst])])
    else:
        return chunk.surface('norm')


def to_root(sentence):
    trees = []
    for chunk in sentence:
        if '名詞' in [m.pos for m in chunk.morphs]:
            trees.append(make_tree(sentence, chunk))
    return trees


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    chunks = nlp.make_chunk(cabocha_file)

    # 確認
    target_line_number = 5
    sentence = next(islice(chunks, target_line_number, None))
    trees = to_root(sentence)
    print('\n'.join(trees))
