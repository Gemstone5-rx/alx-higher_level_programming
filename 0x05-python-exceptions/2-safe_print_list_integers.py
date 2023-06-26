#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    rnum = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            rnum += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (rnum)
