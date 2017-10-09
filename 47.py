# -*- coding: utf-8 -*-
"""
Create on Tue Oct 10 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．
    - 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
    - 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，
      最左の動詞を用いる
    - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
    - 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる
      （助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．
```
    返事をする      と に は        及ばんさと 手紙に 主人は
```
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
    - コーパス中で頻出する述語（サ変接続名詞+を+動詞）
    - コーパス中で頻出する述語と助詞パターン

@author t-take
"""

import os
from itertools import islice
import nlp


def sahen_wo(chunk):
    surface = ''
    sahen_morphs = filter(lambda m: m.pos1 == 'サ変接続', chunk.morphs[:-1])
    for i, morph in enumerate(sahen_morphs):
        if (len(chunk.morphs) > i
            and chunk.morphs[i + 1].surface == 'を'):
            surface = morph.surface + chunk.morphs[i + 1].surface
            break
    return surface


def case_analysis3(sentence):
    cases = []
    for chunk in sentence:
        surface = sahen_wo(chunk)
        if surface:
            dst_chunk = sentence[chunk.dst]
            try:
                morph = next(filter(
                    lambda m: m.pos == '動詞', dst_chunk.morphs))
            except StopIteration:
                continue
            else:
                srcs = list(map(lambda s: sentence[s], dst_chunk.srcs))
                srcs.remove(chunk)
                part = [str(m) for s in srcs for m in s.morphs if m.pos == '助詞']
                if part != []:
                    cases.append([surface + morph.base, sorted(part),
                                  sorted([s.surface('norm') for s in srcs])])
    return cases


def chunks2casetxt3(chunk_list, output_file):
    with open(output_file, 'w') as f:
        for sentence in chunk_list:
            cases = case_analysis3(sentence)
            if cases:
                f.writelines(map(lambda x: '{}\t{}\t{}\n'.format(
                    x[0], ' '.join(x[1]), ' '.join(map(str, x[2]))), cases))


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    case_file = nlp.output('neko.txt.case.sahen_wo')

    chunks = nlp.make_chunk(cabocha_file)
    chunks2casetxt3(chunks, case_file)

    # 確認
    display_count = 5
    relpath = './' + os.path.relpath(case_file)

    command = "cut -d '\t' -f 1 {} | sort | uniq -c | sort -nr -k1 | head -n {}"
    nlp.unix(command.format(relpath, display_count))

    command = "cut -d '\t' -f 1,2 {} | sort | uniq -c | sort -nr -k1 | head -n {}"
    nlp.unix(command.format(relpath, display_count))
