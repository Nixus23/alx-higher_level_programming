#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        count = len(sentence)
        char = sentence[0]
        tup = (count, char)
        return tup
