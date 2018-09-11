# Euler Third Problem
# Holden Stringfield
# This returns the largest prime factor of a number

def main():
  num = int(input("What is the number? "))
  comp(num)

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

def sol(num):
    i = 2
    while i * i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    print(num)

main()