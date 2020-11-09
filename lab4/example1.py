#Write a Python program that asks the user for an integer and prints the sum of the last two digits of the number.Note: If it is a single-digit number, assume it has 0 at the beginning, e.g. 07 for 7.
number1 = int(input('Enter your first integer'))
number2 = int(input('Enter your second integer'))
if number1 < 10 and number2 < 10 :
  print(number1 + number2)
elif number1 < 10 and (number2 > 10 or (number2 > 10 and number2 < 100)) :
  print(number1 + number2)
elif number2 < 10 and (number1 > 10 or (number1 > 10 and number1 < 100)) :
  print(number1 + number2)
elif (number1 > 10 and number1 < 100) and (number2 > 10 and number2 < 100) :
  print(number1 + number2)
elif (number1 < 10 and number2 > 100 ) or (number2 < 10 and number1 > 100) :
  print(number1 + (number2 % 100))
elif ((number1 > 10 and number1 < 100 ) and number2 > 100 ) :
  print(number1 + (number2 % 100))
elif ((number2 > 10 and number2 < 100 ) and number1 > 100 ) :
  print(number2 + (number1 % 100))
else :
  print((number1 % 100) + (number2 % 100))