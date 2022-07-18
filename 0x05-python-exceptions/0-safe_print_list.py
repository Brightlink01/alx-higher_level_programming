#r/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x counts the number of element to be printed
The number of elements printed.
"""
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
        print("")
        return (ret)
