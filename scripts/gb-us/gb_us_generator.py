#!/usr/bin/env python

from nltk.corpus import wordnet

def similarity(left, right, sim=wordnet.path_similarity):
    left_syn_set = wordnet.synsets(left)
    right_syn_set = wordnet.synsets(right)
    sim_gen = (sim(l, r) for l in left_syn_set for r in right_syn_set)
    max_sim = 0
    for s in sim_gen:
        max_sim = max(max_sim, s)
    return max_sim

gb2us_spec = [('our', 'or'), ('re', 'er'), ('ce', 'se'), ('xion', 'ction'), ('ise', 'ize'), ('isation', 'ization'), ('yse', 'yze'), ('ogue', 'og')]

def gb2us(word):
    for gb, us in gb2us_spec:
        if word.endswith(gb):
            return word[:-len(gb)] + us
    return word

def gen_synonyms(lines):
    for line in lines:
        all_word = line.strip()
        if all_word[0].isupper() or any([ord(c) > 128 for c in all_word]):
            continue
        potential_us = gb2us(all_word)
        if potential_us == all_word:
            continue
        sim = similarity(all_word, potential_us)
        if sim == 1.0:
            yield (all_word, potential_us)

