# -*- coding: utf-8 -*-
"""
Create on Wed Oct 04 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．

@author t-take
"""

import nlp


class Chunk(nlp.Chunk):
    """分節表現
    句読点などの記号を含まない表層系の出力を持つ"""
    def __init__(self, dependency=None, morph_list=[]):
        super(Chunk, self).__init__(dependency, morph_list)

    def surface(self, stype='normalize'):
        """表層系
        type : ['full', 'normalize']"""

        if stype[:4] == 'full':
            return ''.join(map(str, self.morphs))

        elif stype[:4] == 'norm':
            return ''.join(
                map(str, filter(lambda m: m.pos != '記号', self.morphs)))


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    cabocha_tsv = nlp.output('neko.txt.tsv')

    chunk_data = nlp.make_chunk(cabocha_file)

    with open(cabocha_tsv, 'w') as f:
        for chunks in chunk_data:
            for ch in filter(lambda c: str(c) != '　', chunks):
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
