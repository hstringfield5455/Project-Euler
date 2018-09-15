# Euler First Problem
# Holden Stringfield
# This program will return sum of the values that are multiples of 3 or 5 under a given value

def main():
    num = int(input("What is the value? "))
    mult(num)


def mult(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

main()