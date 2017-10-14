# -*- coding: utf-8 -*-
"""
Create on Sun Oct 15 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

55. 固有表現抽出
入力文中の人名をすべて抜き出せ．

@author t-take
"""
from __future__ import division, absolute_import, print_function

import xml.etree.ElementTree as ET
import nlp


def person_names(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    names = []
    for token in root.iter('token'):
        if token.findtext('NER') == 'PERSON':
            names.append(token.findtext('word'))
    return names


if __name__ == '__main__':

    xml_file = nlp.get('nlp.txt.xml')

    names = person_names(xml_file)

    print(names)
