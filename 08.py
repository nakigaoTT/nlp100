# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．

@author t-take
"""


def cipher(sentence):
    return ''.join([chr(219 - ord(c)) if 'a' <= c <= 'z' else c
                    for c in sentence])


if __name__ == '__main__':

    sentence = 'The jumping fox...'
    coded = cipher(sentence)
    decoded = cipher(coded)

    print('  input: %s' % sentence)
    print('  coded: %s' % coded)
    print('decoded: %s' % decoded)
