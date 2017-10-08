# -*- coding: utf-8 -*-
"""
Create on Sun Oct 08 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
ただし，出力は以下の仕様を満たすようにせよ．
    - 動詞を含む文節において，最左の動詞の基本形を述語とする
    - 述語に係る助詞を格とする
    - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
```
    始める  で
    見る    は を
```
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
    - コーパス中で頻出する述語と格パターンの組み合わせ
    - 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

@author t-take
"""

import os
from itertools import islice
import nlp


def case_analysis(sentence):
    cases = []
    for chunk in sentence:
        try:
            morph = next(filter(lambda m: m.pos == '動詞', chunk.morphs))
        except StopIteration:
            continue
        else:
            srcs = map(lambda s: sentence[s], chunk.srcs)
            part = [str(m) for s in srcs for m in s.morphs if m.pos == '助詞']
            if part != []:
                cases.append([morph.base, part])
    return cases


def chunks2casetxt(chunk_list, output_file):
    with open(output_file, 'w') as f:
        for sentence in chunk_list:
            cases = case_analysis(sentence)
            f.writelines(
                map(lambda x: '{}\t{}\n'.format(x[0], ' '.join(x[1])), cases))


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    case_file = nlp.output('neko.txt.case')

    chunks = nlp.make_chunk(cabocha_file)
    chunks2casetxt(chunks, case_file)

    # 確認
    display_count = 5
    relpath = './' + os.path.relpath(case_file)

    command = 'sort {} | uniq -c | sort -nr -k1 | head -n {}'
    nlp.unix(command.format(relpath, display_count))

    command = 'grep "{}" {} | sort | uniq -c | sort -nr -k1 | head -n {}'
    for target in ['する', '見る', '与える']:
        nlp.unix(command.format(target, relpath, display_count))
