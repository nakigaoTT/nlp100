# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序を
ランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I
was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．

@author t-take
"""

import random


def typoglycemia(sentence, seed=None):
    if seed is not None:
        random.seed(seed)

    shuffled = []
    for word in sentence.split(' '):
        if len(word) > 4:
            x = [c for c in word[1:-1]]
            random.shuffle(x)
            word = word[0] + ''.join(x) + word[-1]
        shuffled.append(word)

    return ' '.join(shuffled)


if __name__ == '__main__':

    sentence = ("I couldn't believe that I could actually understand what "
                "I was reading : the phenomenal power of the human mind .")

    print(typoglycemia(sentence))
