#Assume that there is a company with 5 employees. ●Take each employee’s name and salary from the user, and store them in a dictionary “employees”.●Print the names of the employees with the highest three salaries.

employees = {}
salarys = []
for x in range(5) :
  name = str(input("Enter your name :"))
  salary = int(input("Enter your salary :"))
  employees.update({name:salary})
  salarys.append(salary)
salarys.sort(reverse=True)
count = 0
while count <3:
  for key, value in employees.items(): 
    if salarys[count] == value: 
      print(key) 
  count = count+1




