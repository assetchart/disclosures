import sys

from disclosures.disclosures import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
