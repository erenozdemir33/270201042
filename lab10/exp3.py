
def sum_number(n):
  if n <= 1 :
    return n
  else :
    return n + sum_number(n-1)


x = sum_number(6)
print(x)
