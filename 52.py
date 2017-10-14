# -*- coding: utf-8 -*-
"""
Create on Sun Oct 15 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

@author t-take
"""
from __future__ import division, absolute_import, print_function

from itertools import islice
import snowballstemmer
import nlp


def word_stem(word):
    stemmer = snowballstemmer.stemmer('english')
    return [word, stemmer.stemWord(word)]


if __name__ == '__main__':

    import importlib
    one_sentence_writer = importlib.import_module('50').one_sentence_writer
    split_word = importlib.import_module('51').split_word

    en_txt = nlp.get('nlp.txt')
    writer = one_sentence_writer(en_txt)

    target_line_number = 5
    sentence = next(islice(writer, target_line_number, None))
    words_list = split_word(sentence)

    for word in words_list:
        print('\t'.join(word_stem(word)))
