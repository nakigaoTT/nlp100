# -*- coding: utf-8 -*-
"""
Create on Wed Oct 11 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．

@author t-take
"""

from itertools import islice
import nlp


def split_word(sentence):
    for word in sentence.split(' '):
        yield word.rstrip('.,;:?!')     # 終端の区切り文字は除去
    yield ''


if __name__ == '__main__':

    import importlib
    one_sentence_writer = importlib.import_module('50').one_sentence_writer

    en_txt = nlp.get('nlp.txt')
    writer = one_sentence_writer(en_txt)

    target_line_number = 5
    sentence = next(islice(writer, target_line_number, None))
    words_list = split_word(sentence)

    for word in words_list:
        print(word, '\n')
