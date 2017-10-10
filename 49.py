# -*- coding: utf-8 -*-
"""
Create on Tue Oct 10 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号が
iとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
    - 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
      （表層形の形態素列）を"->"で連結して表現する
    - 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．
    - 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
    - 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
      文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
      文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．
```
    Xは | Yで -> 始めて -> 人間という -> ものを | 見た
    Xは | Yという -> ものを | 見た
    Xは | Yを | 見た
    Xで -> 始めて -> Y
    Xで -> 始めて -> 人間という -> Y
    Xという -> Y
```

@author t-take
"""

from itertools import islice, combinations
import nlp


# def make_path(sentence, x_chunk, y_chunk, chunk=None):
#
#     if chunk is None:   # * 始端
#         if x_chunk is not None:     # xの始端
#             rep_morph = next(filter(lambda m: m.pos == '名詞', x_chunk.morphs))
#             x_surface = x_chunk.surface('norm').replace(str(rep_morph), 'X')
#             dst_chunk = sentence[x_chunk.dst]
#             return ' '.join([x_surface,
#                              make_path(sentence, None, y_chunk, dst_chunk)])
#         else:                       # yの始端
#             rep_morph = next(filter(lambda m: m.pos == '名詞', y_chunk.morphs))
#             y_surface = y_chunk.surface('norm').replace(str(rep_morph), 'Y')
#             dst_chunk = sentence[y_chunk.dst]
#             return ' '.join([y_surface,
#                              make_path(sentence, x_chunk, None, dst_chunk)])
#
#     elif chunk.dst > 0:
#         if y_chunk is not None and chunk.num == y_chunk.num:    # X -> Y
#             return ' '.join(['->', 'Y'])
#         else:                           # 探索の継続
#             dst_chunk = sentence[chunk.dst]
#             return ' '.join(['->', chunk.surface('norm'),
#                              make_path(sentence, x_chunk, y_chunk, dst_chunk)])
#
#     else:               # * 終端
#         if y_chunk is not None:     # Yの探索を開始
#             return ' '.join(['|', make_path(sentence, x_chunk, y_chunk, None)])
#         else:
#             return ' '.join(['|', chunk.surface('norm')])



def make_path(sentence, x_chunk, y_chunk, chunk=None):

    if chunk is None:   # * 始端

        if x_chunk is not None:     # Xの始端
            chunk = x_chunk
            x_chunk = None
            char = 'X'
        else:                       # Yの始端
            chunk = y_chunk
            y_chunk = None
            char = 'Y'

        # rep_morph = next(filter(lambda m: m.pos == '名詞', chunk.morphs))
        # surface = chunk.surface('norm').replace(str(rep_morph), char)
        char = [''] * len(chunk.morphs) + list(char)
        surface = ''.join([char.pop() if m.pos == '名詞' else (str(m) if m.pos != '記号' else '') for m in chunk.morphs])
        dst_chunk = sentence[chunk.dst]
        return ' '.join([surface,
                         make_path(sentence, x_chunk, y_chunk, dst_chunk)])

    elif chunk.dst > 0:

        if y_chunk is not None and chunk.num == y_chunk.num:    # X -> Y
            return ' '.join(['->', 'Y'])
        else:                           # 探索の継続
            dst_chunk = sentence[chunk.dst]
            return ' '.join(['->', chunk.surface('norm'),
                             make_path(sentence, x_chunk, y_chunk, dst_chunk)])

    else:               # * 終端

        if y_chunk is not None:     # Yの探索を開始
            return ' '.join(['|', make_path(sentence, x_chunk, y_chunk, None)])
        else:
            return ' '.join(['|', chunk.surface('norm')])


def relate_path(sentence):
    paths = []
    noun_chunks = list(filter(
        lambda chunk: '名詞' in [m.pos for m in chunk.morphs], sentence))
    for x_chunk, y_chunk in combinations(noun_chunks, 2):
        paths.append(make_path(sentence, x_chunk, y_chunk))
    return paths


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    chunks = nlp.make_chunk(cabocha_file)

    # 確認
    target_line_number = 5
    sentence = next(islice(chunks, target_line_number, None))
    print(sentence)
    rpath = relate_path(sentence)
    print('\n'.join(rpath))
