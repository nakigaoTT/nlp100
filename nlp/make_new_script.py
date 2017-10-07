#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Create on Mon Oct 2 2017
Generate a script written with the probrems of "言語処理100本ノック 2015".
Last update: Sat Oct 7 2017
@author t-take
"""

import re
import json
import glob
import subprocess
from os.path import join, dirname, splitext, basename
from datetime import datetime


json_file = join(dirname(__file__), 'datas.json')
with open(json_file, 'r') as f:
    jdata = json.load(f)
CORPUS_DIR = jdata.pop('directorys')['corpus']
CORPUS_FILE = {key: join(dirname(__file__), CORPUS_DIR, value)
               for key, value in jdata.items()}


def next_probrem(dir_path):
    """Return a number of next question from *.py file in current directory.
    """
    pyfile = map(lambda x: splitext(basename(x))[0],
                 glob.glob(join(dir_path, '*.py')))
    last_num = sorted(filter(lambda x: x.isdigit(), pyfile))[-1]
    return str(int(last_num) + 1).zfill(2)


def probrem_doc(num, all_problem_file=CORPUS_FILE['nlp_questions']):
    """Get a text of the question."""
    with open(all_problem_file, 'r') as f:
        for line in f:
            if re.search(r'第(.+)章:', line):
                doc = []
                line += next(f)     # pass a line feed after "第(.+)章:"
                while line != '\n':
                    doc.append(line)
                    line = next(f)
                doc.append('\n')
            if line[:2] == num:
                while line != '\n':
                    doc.append(line)
                    line = next(f)
                break
    return ''.join(doc)


def write(file_name, doc='', template=None):
    """Make a python script file and write a document"""
    if template is None:
        now = datetime.now()
        template = '\n'.join([
            '# -*- coding: utf-8 -*-',
            '"""',
            'Create on {0:%a %b %d %Y}'.format(now),
            '',
            '%s',
            '@author t-take',
            '"""',
            ''])
    if '%s' in template:
        doc = template % doc

    with open(file_name, 'w') as f:
        f.write(doc)


def make_new_file(directory_path='./'):
    next_number = next_probrem(directory_path)
    doc = probrem_doc(next_number)
    write('{}.py'.format(next_number), doc)
    return '{}.py'.format(next_number)


def open_in_atom(file_name):
    subprocess.call(['atom', file_name])


if __name__ == '__main__':
    open_in_atom(make_new_file())
