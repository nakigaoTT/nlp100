# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

@author t-take
"""


def n_gram(sequence, n=1):
    if isinstance(sequence, str):
        sequence = sequence.replace(' ', '')
    i = 0
    while i <= len(sequence) - n:
        yield sequence[i:i+n]
        i += 1


if __name__ == '__main__':

    sentence = 'I am an NLPer'

    print(list(n_gram(sentence, 2)))
    print(list(n_gram(sentence.split(' '), 2)))
