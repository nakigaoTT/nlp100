# -*- coding: utf-8 -*-
"""
Create on Mon Oct 02 2017

第4章: 形態素解析

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

MeCabインストール:
    https://qiita.com/taroc/items/b9afd914432da08dafc8

30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．

@author t-take
"""

import MeCab
import nlp


def parse_sentence(mecab_file):
    """構文解析された.mecabファイルから１文ずつリスト化する"""
    morpheme_list = []
    f = open(mecab_file, 'r')

    for line in f:
        # 要素の抽出
        if '\t' not in line:    # タブ区切りがない場合はスルー
            continue
        surface, feature = line.split('\t')
        feature = feature.split(',')
        morpheme = {
            'surface': surface,
            'base': feature[6],
            'pos': feature[0],
            'pos1': feature[1],
        }

        blank = (morpheme['surface'] == '　')    # 空白文字か
        eos = (morpheme['surface'] == '。')      # 句末か

        if not blank:   # 空白文字は追加しない
            morpheme_list.append(morpheme)

        if any((blank, eos)) and morpheme_list != []:
            yield morpheme_list        # 要素を持ち空白か句末なら返却
            morpheme_list = []

    else:   # ループ終了時にファイルクローズ
        f.close()
        raise StopIteration


if __name__ == '__main__':

    file_name = nlp.get('neko.txt')
    parse_file_name = nlp.output('neko.txt.mecab')

    # 形態素解析
    with open(file_name, 'r') as rf, open(parse_file_name, 'w') as wf:
        tagger = MeCab.Tagger()
        wf.write(tagger.parse(rf.read()))

    # 解析結果の表示
    parser = parse_sentence(parse_file_name)
    for i, morpheme in enumerate(parser):
        for dic in morpheme:
            print(dic)
        else:
            print('-----')
        if i >= 3:
            break
