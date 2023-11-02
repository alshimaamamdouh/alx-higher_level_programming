#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argss = len(sys.argv) - 1
    j = 1
    if argss == 0:
         print("{} arguments.".format(argss))
    elif argss == 1:
        print("{} argument:".format(argss))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argss))
        for i in sys.argv:
            print("{}: {}".format(j, i))
        j += 1
