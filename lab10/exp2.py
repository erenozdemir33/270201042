#Write  a  function  that  takes a  number  n  and prints  numbers  starting from  n  to  1  in  a recursive manner.•Change the function to print numbers starting from 1 to n in a recursive manner.

def rec_func(n):
  if n == 0 :
    return 
  else :
    print(n)
    return  rec_func(n-1) 

rec_func(6)

count = 1
def reverse_rec_func(n,count) :
  if n == 0 :
    return
  else :
    count += 1
    print(count)
    return reverse_rec_func(n-1,count)
  
reverse_rec_func(5,count)


    


