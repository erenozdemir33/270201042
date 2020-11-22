#Write a Python program which calculates n factorial where n is given by the user.
number = int(input("Enter your integers to calculate its factorial:"))
value = 1
for x in range(number):
  value = value * (x+1)
print("Factorial : ", value)