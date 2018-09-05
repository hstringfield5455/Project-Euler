# Euler Sixth Problem
# Holden Stringfield
# This program will find the difference between the sum of the squares and the square of the sums of a set of numbers

def main():
  sqosu = 0
  for i in range(100):
    i += 1 
    sqosu += i
  sqosu = sqosu ** 2

  suosq = 0
  for i in range(100):
    i += 1
    suosq += (i ** 2)

  print(sqosu - suosq)
