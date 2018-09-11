# Euler Third Problem
# Holden Stringfield
# This returns the largest prime factor of a number

def main():
    num = int(input("What is the number? "))
    max_factor(num)

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i== 0:
            return False

    return True

def comp(num):
    if isPrime(num) == True:
        print("It is prime")
        return
    else:
        i = 2
        larg = 0
        while i < (num - 1):
            if num % i == 0:
                if isPrime(i) == True:
                    larg = i
            i += 2
        if num % 2 == 0:
            if 2 > larg:
                larg = 2

        print(larg)

def max_factor(num):
    """Find the maximum prime factor."""
    factor = 2
    while factor * factor <= num:
        while num % factor == 0:
            best = factor
            num /= factor
        factor += 1
    if num > 1:
        print(num)
    print(best)

main()