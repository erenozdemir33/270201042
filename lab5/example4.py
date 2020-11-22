#Write a Python program that asks the user for a password as soon as he/she enters the right password.Display “Wrong” when password and input don’t match. Display the first letter of the password when input is “help”. Display “Welcome” and exit when input and password match.
result = 0
password = input('Save your password here :')
n = input('Enter your password :')
if n == 'help' :
  list(password)
  print(password[0])
elif password != n :
  print('“Wrong”')
elif password == n :
  print('Welcome')