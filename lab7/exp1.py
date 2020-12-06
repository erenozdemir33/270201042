#Print the names●You’re given a tuple of name and age for everyone in a group. Print out the names of people who are older than 18.●For example:○input: [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]○output: NedCatelyn

my_tuple = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

for i in range(5) :
  if (my_tuple[i])[1] > 18 :
    print((my_tuple[i])[0])
  else : 
    pass
 