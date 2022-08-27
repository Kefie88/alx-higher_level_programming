#!/usr/bin/python3
def multiple_return(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return(tup)
