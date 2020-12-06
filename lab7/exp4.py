#Check a Password●Write a Python program that determines and prints whether a password is valid or not. ●A valid password is at least 8 characters longand  contains  at  least one  uppercase  letter (A-Z),  at  least one  lowercase  letter  (a-z), and at least one number (0-9). 

password = str(input("Enter a valid password"))

if len(password) < 8 :
  print("your password is not valid")

numbers = "0123456789"
count3 = 0
count2 = 0
count1 = 0
for x in password :
  if x in numbers :
    count3 = count3 + 1
  elif x == x.upper() :
    count1 = count1 + 1
  elif x == x.lower() :
    count2 = count2 + 1


if (count1 > 1) and (count2 > 1) and (count3 > 1) :
  print("your password is valid")
else :
  print("your password is not valid")




  

