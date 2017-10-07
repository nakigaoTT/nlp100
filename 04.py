# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also
Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

@author t-take
"""


if __name__ == '__main__':

    sentence = ('Hi He Lied Because Boron Could Not Oxidize Fluorine.'
                ' New Nations Might Also Sign Peace Security Clause.'
                ' Arthur King Can.')

    one_char = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    chemical_symbol = {c[:1] if i + 1 in one_char else c[:2]: i + 1
                       for i, c in enumerate(sentence.split(' '))}

    print(chemical_symbol)
