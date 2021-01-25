str1 = input("Enter your word:")
str2 = input("Enter your word:")


def find_anagram_or_not(str1,str2) :
  if sorted(str1) == sorted(str2) :
    print("This words are anagram.")
  else :
    print("This words are not anagram")

find_anagram_or_not(str1,str2)

def merge(lst1, lst2, lst3): # merge sorted lst1 and lst2 into lst3# these indexes keep track of current position in each list 
i1, i2, i3 = 0, 0, 0 # all start at the front
n1, n2 = len(lst1), len(lst2)# Loop while both lst1 and lst2 have more items
while i1 < n1 and i2 < n2:
  if lst1[i1] < lst2[i2]:# top of lst1 is smaller
  lst3[i3] = lst1[i1]# copy it into current spot in lst3
  i1 = i1 + 1
  else: # top of lst2 is smaller
  lst3[i3] = lst2[i2] # copy it into current spot in lst3
  i2 = i2 + 1
  i3 = i3 + 1# item added to lst3, update position# Here either lst1 or lst2 is done. One of the following loops# will execute to finish up the merge.
  while i1 < n1:# Copy remaining items (if any) from lst1
  lst3[i3] = lst1[i1]i1 = i1 + 1i3 = i3 + 1    
  while i2 < n2:# Copy remaining items (if any) from lst2
  lst3[i3] = lst2[i2]
  i2 = i2 + 1
  i3 = i3 + 1
  print(list3)