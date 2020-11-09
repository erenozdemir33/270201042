#Write a Python program that asks the user for two integers a and b and calculates ab without using ** operator and pow function.
a = int(input('Enter your a integer'))
b = int(input('Enter your b integer'))
result = 1
print(range(b))
for x in range(b) :
  result = a * result
print(result)
