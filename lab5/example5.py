#Write a Python program that asks the user how many Fibonacci numbers to generate and then displays them.
a = int(input("Range of fibonacci: "))
n1 = 0
n2 = 1

for i in range(a):
  n3 = n2+n1
  n1 = n2
  n2 = n3
  print(n1)