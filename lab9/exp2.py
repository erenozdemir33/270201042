def get_reversed(list1) :
  if len(list1) == 0:
    return []
  else :
    return [list1[-1]] + get_reversed(list1[:-1])
  
print(get_reversed([1,2,3,4,5]))