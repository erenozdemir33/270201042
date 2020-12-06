n = str(input("Enter your input"))
lower_n = n.lower()
count = 0
vowels = ["a" , "e" , "ı", "i" ,"o" , "ö", "u","ü"]
for x in lower_n :
  if x in vowels :
    count = count + 1
print(count)
