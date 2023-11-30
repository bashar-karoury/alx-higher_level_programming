#!/usr/bin/python3
import calculator_1
import sys
add = calculator_1.add
sub = calculator_1.sub
mul = calculator_1.mul
div = calculator_1.div
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
