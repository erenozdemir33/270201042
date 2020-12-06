books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
book_dict_keys = []
book_values = []
i = 0
while i < 4 :
  book_dict_keys.append(books[i])
  i = i + 1
print(book_dict_keys)

no = []
for x in range(4) :
  unique = set(books[x])
  no.append(len(unique))


first_no = []
for y in range(4):
  first_no.append(len(books[y]))


value = list(zip(first_no,no))
print(value)

for i in range(4) :
  book_dict[book_dict_keys[i]] = value[i]
print(book_dict)


average = []
for i in range(4) :
  average.append(int(sum(value[i]) / 2))
print(average)

new_value = list(zip(first_no,no,average))
print(new_value)

for i in range(4) :
  book_dict[book_dict_keys[i]] = new_value[i]

for key,value in book_dict.items() :
  print(key, " : " ,value)





