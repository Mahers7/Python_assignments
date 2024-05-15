import sys
def main():
    if len(sys.argv) !=2:
        exit("Usage: {sys.argv[0]}  NUMBER for factorial")

    n = int(sys.argv[1])
    result = factorial(n)
    print("{n} {result}")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

main()

