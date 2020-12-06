#Write a program that gets a number n and build the identity matrix, then print it. E.g
inputNum = int(input("Insert the number to build an identity matrix. "))
matrix = []
counter = 1
for x in range(inputNum) :
  matrix = []
  for y in range(1, inputNum + 1) :
    if y == counter :
      matrix.append(1)
    else :
      matrix.append(0)
  counter += 1
  print(matrix)