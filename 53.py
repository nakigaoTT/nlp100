# -*- coding: utf-8 -*-
"""
Create on Sun Oct 15 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

@author t-take
"""
from __future__ import division, absolute_import, print_function

import xml.etree.ElementTree as ET
import nlp


def xml2word(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for word in root.iter('word'):
        yield word.text


if __name__ == '__main__':

    xml_file = nlp.get('nlp.txt.xml')

    writer = xml2word(xml_file)

    for word in writer:
        print(word)
