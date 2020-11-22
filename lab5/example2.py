#Write a Python program that takes N integers from user and displays % of even ones. Hint: Take N from user at the beginning and use it to create a loop
count = 0 
n = int(input('How many integers do you have?'))
for i in range(n) :
  x = int(input('Enter your integer'))
  if x % 2 == 0 :
    count = count + 1
    print((count * 100 ) / n )