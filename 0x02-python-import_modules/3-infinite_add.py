#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = 1
    net = 0
    for i in sys.argv:
        if j <= len(sys.argv) - 1:
            net = net + int(sys.argv[j])
            j += 1
    print(net)
