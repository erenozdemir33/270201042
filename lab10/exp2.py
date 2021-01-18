#Write  a  function  that  takes a  number  n  and prints  numbers  starting from  n  to  1  in  a recursive manner.•Change the function to print numbers starting from 1 to n in a recursive manner.

def rec_func(n):
  if n == 0 :
    return 
  else :
    print(n)
    return  rec_func(n-1) 

rec_func(6)


def reverse_rec_func(n) :
  if n == 0 :
    return 
  else :
    n = n + 1
    return reverse_rec_func(n - 2)

print(reverse_rec_func(6))