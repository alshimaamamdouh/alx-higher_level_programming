#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    num = len(sys.argv) - 1
    net = 0
    if num != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    d = sys.argv[2]
    if d != '+' and d != '-' and d != '*' and d != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if d == '+':
        net = add(a, b)
        print("{} + {} = {}".format(a, b, net))
    elif d == '-':
        net = sub(a, b)
        print("{} - {} = {}".format(a, b, net))
    elif d == '*':
        net = mul(a, b)
        print("{} * {} = {}".format(a, b, net))
    else:
        net = div(a, b)
        print("{} / {} = {}".format(a, b, net))
