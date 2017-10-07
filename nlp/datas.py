# -*- coding: utf-8 -*-
"""
Name list of "言語処理100本ノック 2015"'s datas and corpases.
@author t-take
"""

import os
import glob

import nlp


CORPUS_DIR = os.path.join(os.path.dirname(__file__), 'data_and_corpus')
CORPUS_FILE = {
    'artist': 'artist.json.gz',
    'enwiki_small': 'enwiki-20150112-400-r100-10576.txt.bz2',
    'enwiki_big': 'enwiki-20150112-400-r10-105752.txt.bz2',
    'hightemp': 'hightemp.txt',
    'jawiki': 'jawiki-country.json.gz',
    'neko': 'neko.txt',
    'nlp_questions': 'nlp_question100.txt',
    'nlp': 'nlp.txt',
    'analogy': 'questions-words.txt',
    'polarity': 'rt-polaritydata.tar.gz',
    'wordsim': 'wordsim353.zip',
}


def get(file_name):
    if file_name in CORPUS_FILE.values():
        return os.path.join(CORPUS_DIR, file_name)
    elif file_name in [os.path.basename(f)
                       for f in glob.glob(os.path.join(nlp.OUTPUT_DIR, '*'))]:
        return os.path.join(nlp.OUTPUT_DIR, file_name)
    raise ValueError('`%s` is not exist.' % file_name)


def get_file_in_sec(section_number=0, keyword=None):
    """Return the file number using Sec. X."""
    file_paths = {key: os.path.join(CORPUS_DIR, value)
                  for key, value in CORPUS_FILE.items()}
    if keyword is None:
        keyword = {
            2: 'hightemp', 3: 'jawiki', 4: 'neko', 5: 'neko', 6: 'nlp',
            7: 'artist', 8: 'polarity', 9: ['enwiki_big', 'enwiki_small'],
            10: ['analogy', 'wordsim']}[section_number]
    if isinstance(keyword, list):
        return [file_paths[kw] for kw in keyword]
    else:
        return file_paths[keyword]
