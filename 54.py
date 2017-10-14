# -*- coding: utf-8 -*-
"""
Create on Sun Oct 15 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

@author t-take
"""
from __future__ import division, absolute_import, print_function

import xml.etree.ElementTree as ET
import nlp


def word_lemma_pos(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for token in root.iter('token'):
        word = token.findtext('word')
        lemma = token.findtext('lemma')
        pos = token.findtext('POS')
        yield '\t'.join([word, lemma, pos])


if __name__ == '__main__':

    xml_file = nlp.get('nlp.txt.xml')

    writer = word_lemma_pos(xml_file)

    for word in writer:
        print(word)
