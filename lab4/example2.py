#Leap year Write a Python program that asks the user for a year and then it checks whether the entered year is a leap year or not.Note: Leap years are "exactly divisible" by 4 but century years which are not divisible by 400 are not leap years.Examples:100, 1900, 2017 → not leap years4, 400, 1992, 2000→ leap years.
year = int(input('Enter a year'))
if (year % 4) > 0 :
  print('Your year is not leap year it is century year')
elif (year % 4) == 0 :
  print('Your year is a leap year')