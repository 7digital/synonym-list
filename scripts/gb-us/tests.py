#coding: utf-8
import unittest

from gb_us_generator import gen_synonyms

class GenSynonymsTests(unittest.TestCase):
    def test_generates_valid_synonyms(self):
        expected_spellings = [('behaviour', 'behavior')
                , ('centre', 'center')
                , ('defence', 'defense')
                , ('connexion', 'connection')
                , ('organise', 'organize')
                , ('organisation', 'organization')
                , ('analyse', 'analyze')
                , ('catalogue', 'catalog')
                ]
        gb_spellings = (gb for gb, _ in expected_spellings)
        actual_spellings = gen_synonyms(gb_spellings)
        self.assertItemsEqual(actual_spellings, expected_spellings)

    def test_does_not_generate_invalid_synonyms(self):
        no_synonyms = ['four', 'dare', 'pence', 'lease']
        actual_spellings = gen_synonyms(no_synonyms)
        self.assertItemsEqual(actual_spellings, [])

    def test_clean_up_edge_cases(self):
        edge_cases = [' behaviour\n', 'Behaviour', 'béhaviour']
        actual_spellings = gen_synonyms(edge_cases)
        self.assertItemsEqual(actual_spellings, [('behaviour', 'behavior')])
