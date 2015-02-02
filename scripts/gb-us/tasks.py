from __future__ import print_function

import sys
import unittest
import nltk
import tests

from invoke import task
from gb_us_generator import gen_synonyms

@task
def generate(dictionary='/usr/share/dict/british-english', output='../../gb-us-synonyms.txt'):
    nltk.download('wordnet')
    with open(dictionary) as dict_file:
        with open(output, 'w') as output_file:
            for gb, us in gen_synonyms(dict_file):
                output_file.write(gb + ', ' + us + '\n')
                print(gb + ',', us)

@task
def test():
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner().run(suite)
