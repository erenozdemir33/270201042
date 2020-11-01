gpa = float(input('Enter your gpa'))
number_of_lectures = int(input('Enter your number of lectures'))
if (gpa < 2.0 and number_of_lectures < 47) :
  print('Not enough number of lectures and gpa')
elif (gpa >= 2.0 and number_of_lectures < 47 ) :
  print('Not enough number of lectures')
elif (gpa < 2.0 and number_of_lectures >= 47) :
  print('Not enough gpa')
else :
  print('GRADUATED')