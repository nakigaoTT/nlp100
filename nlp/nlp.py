# -*- coding: utf-8 -*-
"""
natural language processing library
===================================

@author t-take
"""

import os
import subprocess
import nlp


# Auxiliary ###################################################################
def output(file_name):
    """Make output directory when nlp.OUTPUT_DIR is noexist
    and return the output file path."""
    if not os.path.isdir(nlp.OUTPUT_DIR):
        os.mkdir(nlp.OUTPUT_DIR)
    return os.path.join(nlp.OUTPUT_DIR, file_name)


def unix(cmd, notice=True):
    """command execution for Sec. 2"""
    if notice:  # show 'cmd' when notice is True
        print('$', cmd)
    subprocess.check_call(cmd, shell=True)


# Natural Language Proecssing #################################################
def parse_sentence(mecab_file):
    """Make a list of morpheme parts for every 1 sentences from .mecab file
    that is parsed. This is made in Q. 30."""
    morpheme_list = []
    f = open(mecab_file, 'r')

    for line in f:
        # The extraction of features.
        if '\t' not in line:    # continue when sentence no have tab separation
            continue
        surface, feature = line.split('\t')
        feature = feature.split(',')
        morpheme = {
            'surface': surface,
            'base': feature[6],
            'pos': feature[0],
            'pos1': feature[1],
        }

        is_blank = (morpheme['pos1'] == '空白')
        is_eos = (morpheme['pos1'] == '句点')

        if not is_blank:   # blank character is not append
            morpheme_list.append(morpheme)

        if any((is_blank, is_eos)) and morpheme_list != []:
            yield morpheme_list     # when it have contents and character is
            morpheme_list = []      # blank or end of phrase, return the list.

    else:   # close the file at finish loop
        f.close()
        raise StopIteration


class Morph(object):
    """Morpheme representation"""
    def __init__(self, morpheme):
        super(Morph, self).__init__()

        self.morpheme = morpheme

        # morpheme extraction
        self.surface, feature = self.morpheme.split('\t')
        feature = feature.split(',')
        self.base = feature[6]
        self.pos = feature[0]
        self.pos1 = feature[1]

    def __repr__(self):
        return '「{}」({}/{})'.format(self.surface, self.pos, self.pos1)

    def __str__(self):
        return self.surface

    def __len__(self):
        return len(self.surface)


def morph_sentence(cabocha_file):
    """Make a list of morpheme class from .cabocha file that is dependency
    analysis by CaboCha. This is made in Q. 40"""
    morpheme_list = []
    f = open(cabocha_file, 'r')

    for line in f:
        # End of sentence
        if line[:3] == 'EOS':
            if morpheme_list:   # If the list have contents, return it.
                yield morpheme_list
                morpheme_list = []
            else:
                continue

        # The extraction of features
        if '\t' not in line or ',' not in line:
            continue    # It is ignore that don't have '\t' or ','
        morpheme = Morph(line)  # set the morpheme
        if morpheme.pos1 != '空白':
            morpheme_list.append(morpheme)

    else:   # close the file at finish loop
        f.close()
        raise StopIteration


class Chunk(object):
    """segment representation
    made in Q. 41. update by Q. 42."""
    def __init__(self, dependency=None, morph_list=[]):
        super(Chunk, self).__init__()
        self.morphs = []
        self.dst = -1
        self.srcs = []

        if dependency is not None:
            dependency = dependency.split(' ')

            if not (len(dependency) == 5
                    and dependency[0] == '*' and dependency[2][-1] == 'D'):
                raise ValueError(
                    'dependency `%s` is invalide format' % dependency)

            self.num = int(dependency[1])       # segment number
            self.dst = int(dependency[2][:-1])  # destination segment number
            _num = dependency[3].split('/')
            self.head_num = int(_num[0])        # primary mopheme number
            self.machine_num = int(_num[1])     # machine language number
            self.score = float(dependency[4])   # segment score

        if morph_list:
            for morpheme in morph_list:
                self.morphs.append(Morph(morpheme))

    def __repr__(self):
        return '[{}]{} {}'.format(
            self.num, self.__str__(),
            '-> [%d]' % self.dst if self.dst != -1 else '-.')

    def __str__(self):
        return ''.join(map(str, self.morphs))

    def __len__(self):
        return len(morphs)

    def surface(self, stype='full'):
        """surface layer form
        type : ['full', 'normalize']"""

        if stype[:4] == 'full':
            return ''.join(map(str, self.morphs))

        # excluding symbols such as punctuation marks
        elif stype[:4] == 'norm':
            return ''.join(
                map(lambda m: str(m) if m.pos != '記号' else '', self.morphs))


def sen2chunk(sentence):
    """Make the Chunk instance that show segmentation from 1 sentence.
    This is made in Q. 41"""
    chunks = []
    morph_list = []

    dependency = sentence[0].replace('\n', '')

    for line in sentence[1:]:

        if line[0] == '*':  # it is show the destination that row started by *
            chunks.append(Chunk(dependency, morph_list))
            dependency = line.replace('\n', '')
            morph_list = []

        else:               # others is show the morpheme
            morph_list.append(line)

    else:
        chunks.append(Chunk(dependency, morph_list))

    # append the destination source on last
    for chunk in chunks:
        dst = chunk.dst
        if dst != -1:
            if chunks[dst].num == dst:
                chunks[dst].srcs.append(chunk.num)

    return chunks


def make_chunk(cabocha_file):
    """Generate the Chunk instances list every 1 sentences.
    This is made in Q. 41."""
    sentence = []
    f = open(cabocha_file, 'r')

    for line in f:

        if line[:3] == 'EOS':
            if sentence:
                yield sen2chunk(sentence)
                sentence = []
            else:
                continue

        else:   # append the line when the line is not 'EOS'
            sentence.append(line)

    else:   # close the file at finish the loop
        f.close()
        raise StopIteration
