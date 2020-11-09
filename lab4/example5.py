#Write a Python program which calculates n factorial where n is given by the user.
sayi = int(input("Enter your integers to calculate its factorial:"))
value = 1
for x in range(sayi):
  value = value * (x+1)
print("Factorial : ", value)