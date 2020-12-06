#Write a program that takes a list of student’s midterm 1, midterm 2 and final exam grades. Then, it calculates and shows each student’s average grade by using the weights 30%, 30% and 40%. Average grades are added into a list. 

#Ask the number of students, and take grades:
#i.e.: [[50,90,60],[15,60,75],[99,95,91], ...]

tot_students = int(input("How many students in the class? :"))
sum = 0
list_sum = []

for x in range(tot_students) :
  mid1_grade = int(input("What is your midterm 1 grade?  :"))
  mid2_grade = int(input("What is your midterm 2 grade ?  :"))
  final_grade = int(input("What is your final exam grade?  :"))
  sum = sum + mid1_grade + mid2_grade + final_grade
  print("Your average grade is" , sum / tot_students)
  average_grade = sum / tot_students
  grade_list = [average_grade]
  list_sum.extend(grade_list)
  print(list_sum)
  


