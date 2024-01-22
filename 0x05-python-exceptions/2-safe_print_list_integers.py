#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ct = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
        except (ValueError, TypeError):
            pass
        else:
            ct += 1
    print()
    return (ct)
