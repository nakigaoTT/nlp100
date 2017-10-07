# -*- coding: utf-8 -*-
"""
Create on Mon Oct 2 2017

第1章: 準備運動

03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving
quantum mechanics."という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

@author t-take
"""


if __name__ == '__main__':

    sentence = ('Now I need a drink, alcoholic of course,'
                'after the heavy lectures involving quantum mechanics.')

    pop_order = sorted(set(p for p in sentence.lower() if 'a' <= p <= 'z'),
                       key=lambda x: sentence.lower().count(x), reverse=True)

    print(pop_order)
