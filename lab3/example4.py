age = int(input('Please enter your age'))
normal_ticket_price = 3
if ( age < 6 and age > 60) :
  print('Your ticket is free')
elif ( age >= 6 and age <= 18) :
  print( normal_ticket_price - (normal_ticket_price * 0.5))
else :
  print(normal_ticket_price)