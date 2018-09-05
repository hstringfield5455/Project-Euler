# Euler Third Problem
# Holden Stringfield
# This returns the largest prim factor of a number

def main():
  num = int(input("What is the number? "))
  comp(num)

def isPrime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False

  return True

def comp(num):
  if isPrime(num) == True:
    print("It is prime")
    return
  for i in range(num-1):
    i += 1
    if isPrime(i) and num % i == 0:
      larg = i
  print(larg)

main()
