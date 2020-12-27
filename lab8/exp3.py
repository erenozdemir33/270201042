def get_rand_list(b,e,N) :
  random_list = []
  for i in range(N):
    import random
    x = random.randint(b,e)
    random_list.append(x)

  return random_list

def get_overlap(list1,list2):
  list1 = set(list1)
  list2 = set(list2)
  z = list1.intersection(list2)
  return z


list1 = get_rand_list(0,10,5)
list2 = get_rand_list(0,10,5)

print(list1)
print(list2)
print(get_overlap(list1,list2))




