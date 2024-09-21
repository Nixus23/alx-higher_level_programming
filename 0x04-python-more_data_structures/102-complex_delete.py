#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    keys = a_dictionary.keys()
    for i in keys:
        if a_dictionary[i] == value:
            delete.append(i)
    for i in delete:
        a_dictionary.pop(i)
    return a_dictionary
