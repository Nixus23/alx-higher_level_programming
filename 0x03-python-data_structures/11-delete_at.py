#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    count = len(my_list)
    if idx >= count or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list