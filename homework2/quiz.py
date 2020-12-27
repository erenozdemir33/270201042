password = "abc123"
i = 0
while i < 3 :
  i = i + 1
  user_password = input("Enter your password")
  if user_password == password :
    print("You have successfully logged in")
    break
  if user_password != password :
    print("Sorry, the password is wrong")
  if i == 3 :
    print("You have been denied access")

