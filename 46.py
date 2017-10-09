# -*- coding: utf-8 -*-
"""
Create on Tue Oct 10 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）
をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
    - 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
    - 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
```
    始める  で      ここで
    見る    は を   吾輩は ものを
```

@author t-take
"""

import os
from itertools import islice
import nlp


def case_analysis2(sentence):
    cases = []
    for chunk in sentence:
        try:
            morph = next(filter(lambda m: m.pos == '動詞', chunk.morphs))
        except StopIteration:
            continue
        else:
            srcs = list(map(lambda s: sentence[s], chunk.srcs))
            part = [str(m) for s in srcs for m in s.morphs if m.pos == '助詞']
            if part != []:
                cases.append([morph.base, part, srcs])
    return cases


def chunks2case2(chunk_list, output_file):
    for sentence in chunk_list:
        cases = case_analysis2(sentence)
        yield map(lambda x: '{}\t{}\t{}\n'.format(
            x[0], ' '.join(x[1]), ' '.join(map(str, x[2]))), cases)


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    case_file = nlp.output('neko.txt.case')

    chunks = nlp.make_chunk(cabocha_file)
    res = chunks2case2(chunks, case_file)

    # 確認
    target_line_number = 5
    target_res = next(islice(res, target_line_number, None))
    for cases in target_res:
        print(cases)
