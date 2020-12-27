def get_evens(list1) :
  if len(list1) == 0 :
    return 0
  else :
    count = 0
    if list1[0] % 2 == 0 :
      count += 1
    return count + get_evens(list1[1:])


print(get_evens([0,1,2,3,4,5,6,7]))


