# Euler Fifth Problem
# Holden Stringfield
# This will return the smallest number with a given range of multiples

i = 0
while i < 2432902008176640000:
  i += 2
  for j in range(20):
    j += 1
    if i % j == 0:
      if j == 20:
        ans = i
      else:
        continue
    else:
      break

print(ans)
