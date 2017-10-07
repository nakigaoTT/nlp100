# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第1章: 準備運動

07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

@author t-take
"""


def temperature_template(x, y, z):
    return ''.join([str(x), '時の', str(y), 'は', str(z)])


if __name__ == '__main__':

    x = 12
    y = '気温'
    z = 22.4

    print(temperature_template(x, y, z))
