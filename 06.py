# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ,
XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

@author t-take
"""

import importlib
n_gram = importlib.import_module('05').n_gram


if __name__ == '__main__':

    sentence1 = 'paraparaparadise'
    sentence2 = 'paragraph'
    n = 2   # bi-gram

    X = set(n_gram(sentence1, n))
    Y = set(n_gram(sentence2, n))

    print('X:', X)
    print('Y:', Y)

    print('Union:', X | Y)
    print('Intersection:', X & Y)
    print('Difference set:', X - Y)
    print("'se' is%s included in X." % ('' if 'se' in X else ' not'))
    print("'se' is%s included in Y." % ('' if 'se' in Y else ' not'))
