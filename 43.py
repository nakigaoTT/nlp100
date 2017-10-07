# -*- coding: utf-8 -*-
"""
Create on Wed Oct 04 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．

@author t-take
"""

import nlp


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    cabocha_tsv = nlp.output('neko.txt.noun2verb.tsv')

    chunk_data = nlp.make_chunk(cabocha_file)

    with open(cabocha_tsv, 'w') as f:
        for chunks in chunk_data:
            for ch in filter(lambda c: str(c) != '　' and c.dst != -1, chunks):
                if not ('名詞' in [x.pos for x in ch.morphs]
                        and '動詞' in [x.pos for x in chunks[ch.dst].morphs]):
                    continue
                f.write('{}\t{}\n'.format(
                    ch.surface('norm'),
                    chunks[ch.dst].surface('norm') if ch.dst != -1 else ''))

    # 確認
    print('係り元の分節\t係り先の分節\n')
    with open(cabocha_tsv, 'r') as f:
        for i, line in enumerate(f):
            print(line)
            if i > 4:
                break
