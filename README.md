# 言語処理100本ノック 2015 演習

[言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/)演習まとめ

## 演習環境
Mac OS X EL Capitan 10.11.6 + Python 3.4.5 :: Continuum Analytics, Inc.

### 追加モジュール

Matplotlib
```Bush:
$ conda install matplotlib
```

MeCab
```Bush:
$ brew install mecab
$ brew install mecab-ipadic
$ pip install mecab-python3
```

CaboCha
```Bush:
$ tar xvfz cabocha-x.xx.tar.bz2
$ cd cabocha-x.xx
$ ./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8
$ make && make check
$ sudo make install
$ cd python
$ python setup.py build
$ python setup.py install
```

GraphViz (Dot言語のグラフ情報から画像ファイルを生成するツール)
```Bush:
$ conda install graphviz
```

pydot-ng
```Bush:
$ conda install pydot-ng
```

snowballstemmer (英語の語幹解析)
```Bush:
$ conda install snowballstemmer
```
