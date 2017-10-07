# -*- coding: utf-8 -*-
"""
Create on Mon Oct 2 2017

第1章: 準備運動

02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

@author t-take
"""

if __name__ == '__main__':

    patrol_car = 'パトカー'
    taxi = 'タクシー'

    mix = ''.join([p + t for p, t in zip(patrol_car, taxi)])

    print(mix)
