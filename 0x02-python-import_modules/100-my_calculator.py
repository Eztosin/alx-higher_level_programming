#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in "+-*/":
        print("Unknown operator.Availaible operators: +, -, * and /")
        sys.exit(1)

    if operator == "+":
        total = add(a, b)
    elif operator == "-":
        total = sub(a, b)
    elif operator == "*":
        total = mul(a, b)
    elif operator == "/":
        total = div(a, b)

    print("{:d} {} {:d} = {:d}".format(a, operator, b, total))
