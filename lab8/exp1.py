#Define a function that takes a list as a parameter and returns the result of the following operation.In main program, print the result of the operation using the list below.
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]

def sum_list(op_list) :
  total = 0
  for i in range(len(op_list)):
    total = total + op_list[i]
  total = float(total)
  squared = total **2
  return squared,total


sum_list(a_list))



