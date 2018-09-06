# Euler Second Problem
# Holden Stringfield
# Returns sum of fibonacci numbers under certain value

def main():
    num = int(input("What is the value? "))
    fibo(num)

def fibo(num):
    sum = 0
    fib1 = 1
    fib2 = 2
    while fib1 < num:
        if fib2 % 2 == 0:
            sum += fib2
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    print(sum)

main()