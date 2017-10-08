# -*- coding: utf-8 -*-
"""
Create on Sat Oct 07 2017

第5章: 係り受け解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．

44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

@author t-take
"""

from itertools import islice
import pydot_ng as pydot
import nlp


def make_graph(chunk_list, save_name):
    graph = pydot.Dot(graph_type='digraph')

    for chunk in chunk_list:
        graph.add_node(pydot.Node(chunk.num, label=chunk.surface('norm')))

    for chunk in filter(lambda c: c.dst >= 0, chunk_list):
        graph.add_edge(pydot.Edge(chunk.num, chunk.dst))

    graph.write_png(save_name)


if __name__ == '__main__':

    cabocha_file = nlp.get('neko.txt.cabocha')
    morph_png = nlp.output('neko_morph_graph.png')

    target_line_number = 3
    chunks_data = nlp.make_chunk(cabocha_file)

    # `target_line_number`番目のchunkを取得
    target_chunks = next(islice(chunks_data, target_line_number, None))

    make_graph(target_chunks, morph_png)
