#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxim = max(a_dictionary.values())
        for i, value in a_dictionary.items():
            if value == maxim:
                return i
    return None
