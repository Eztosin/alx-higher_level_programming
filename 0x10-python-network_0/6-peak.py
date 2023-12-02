#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers: list of integers to find peak of
    Returns: Peak of list_of_integers or None
    """
    if not list_of_integers:
        return None
    results = []
    high = len(list_of_integers) - 1
    # for i in range(1, high):
    #     if (list_of_integers[i] > list_of_integers[i - 1] and
    #     list_of_integers[i] > list_of_integers[i + 1]):
    #        results.append(list_of_integers[i])
    #     elif (list_of_integers[i] == list_of_integers[i - 1] and
    #     list_of_integers[i] == list_of_integers[i + 1]):
    #        results.append(list_of_integers[i])
    # return results
    for i in range(0, high):
        if (list_of_integers[i] > list_of_integers[i - 1] and
                list_of_integers[i] > list_of_integers[i + 1]):
            results.append(list_of_integers[i])
        elif (list_of_integers[i] == list_of_integers[i - 1] and
                list_of_integers[i] == list_of_integers[i + 1]):
            results.append(list_of_integers[i])
    return max(results)
