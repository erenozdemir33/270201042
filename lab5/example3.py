#Write a Python program that asks the user for two positive integers and finds the number of matching digits (starting from units digit).
int_1 = input('Enter your first integer')
int_2 = input('Enter your second integer')
if int(int_1) > 0 and int(int_2) > 0 :
  count = 0
  result = 0
  if len(int_1) >= len (int_2) :
    count = len(int_2)
  else :
    count = len(int_1)
  int_1 = int_1[::-1] 
  int_2 = int_2[::-1]
  for x in range(count - 1):
    if int_1[x] == int_2[x] :
      result = result + 1
  print(result)
else : 
  print('Please enter positive integers')