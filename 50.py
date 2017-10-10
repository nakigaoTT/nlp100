# -*- coding: utf-8 -*-
"""
Create on Tue Oct 10 2017

第6章: 英語テキストの処理

英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，
入力された文書を1行1文の形式で出力せよ．

@author t-take
"""

import nlp


def one_sentence_writer(english_txt_file):
    f = open(english_txt_file, 'r')

    for line in filter(lambda l: l != '', map(lambda l: l.rstrip(), f)):
        # 改行コードは削除，空行は飛ばす

        index = -1
        while True:
            index = line.find(' ', index + 1)
            if index < 0:   # 一致する部分がなるくなると str().find() は -1 を返す
                break

            if (line[index - 1] in ['.', ';', ':', '?', '!']
                and line[index + 1].isupper()):
                one_sentence, line = line[:index], line[index + 1:]
                yield one_sentence

        yield line

    else:
        f.close()
        return StopIteration


if __name__ == '__main__':

    en_txt = nlp.get('nlp.txt')

    writer = one_sentence_writer(en_txt)

    # 確認
    for sentence in writer:
        print(sentence, '\n')
