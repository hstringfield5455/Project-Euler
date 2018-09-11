# Euler Fourth Problem
# Holden Stringfield
# This will find the largest palindrome 

def main():
    i = 1000
    while i > 99:
        i -= 1
        j = 1000
        while j > 99:
            j -= 1
            if str(i*j) == str(i*j)[::-1]:
                print(i*j)
                break
