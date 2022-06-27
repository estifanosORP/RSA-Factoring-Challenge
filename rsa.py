#!/usr/bin/python3
import sys


def isprime(num):
    """
    checks if a number is a prime number
    """
    for x in range(2, int(num/2)):
        if num % x == 0:
            return False
    return True


def factors(num):
    """
    expresses a number as a multiple of two
    prime numbers
    """
    for x in range(2, int(num/2)):
        if num % x == 0:
            if isprime(x) and isprime(int(num/x)):
                return (x, int(num/x))

    return (num, 1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Only one file name should be used as an argument")
        sys.exit(0)

    file_name = sys.argv[1]

    with open(file_name, 'r') as f:
        lines = f.readlines()

    for x in lines:
        a, b = factors(int(x))
        print("{}={}*{}".format(int(x), b, a))
