
def rec_multipication(n) :
  if n == 0 :
    return n + 1
  else :
    return n + rec_multipication(n - 1)

x = rec_multipication(3)
print(x)
