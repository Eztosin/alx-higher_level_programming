#!/usr/bin/python3
"""prints a text"""


def text_indentation(text):
    """prints a text with two lines after special characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    str_len = len(text)
    i = 0

    while i < str_len:
        if text[i] in ('.', '?', ':'):
            if (i + 1) != str_len or (i + 1) != ' ':
                new_text = text[i + 1]
                if new_text not in ('.', '?', ':'):
                    print("{}".format(text[i]), end='\n\n')
                    if new_text == ' ':
                        i += 2
                    if new_text != ' ':
                        i += 1
        else:
            print("{}".format(text[i]), end='')
            i += 1
