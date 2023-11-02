#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argss = len(sys.argv) - 1
    if argss == 0:
         print("{} arguments.".format(argss))
    elif argss == 1:
        print("{} argument:".format(argss))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argss))
        j = 1
        for i in sys.argv:
            if j <= argss:
                print("{}: {}".format(j, sys.argv[j]))
                j += 1
