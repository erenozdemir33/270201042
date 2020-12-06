#quiz5
name = input("enter your name") 
for i in name.upper() :
  print(i)

a = ""
while True :
  string = str(input("Please enter any string : "))
  if string == "quit" :
    break
  else :
    a = a + string
print(a)


