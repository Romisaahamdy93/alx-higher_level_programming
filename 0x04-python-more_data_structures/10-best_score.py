#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bigscore = 0
    bigkey = None
    for k, s in a_dictionary.items():
        if s > bigscore:
            bigscore = s
            bigkey = k
    return bigkey
