#Write another program that puts average grades that are greater than 90 into a list.

tot_students = int(input("How many students in the class? :"))
sum = 0
list_sum = []

for x in range(tot_students) :
  mid1_grade = int(input("What is your midterm 1 grade?  :"))
  mid2_grade = int(input("What is your midterm 2 grade ?  :"))
  final_grade = int(input("What is your final exam grade?  :"))
  if (mid1_grade > 100) or (mid2_grade > 100) or (final_grade > 100):
    print("not accepted")
  else :

    sum = sum + mid1_grade + mid2_grade + final_grade
    print("Your average grade is" , sum / tot_students)
    if (sum / tot_students) > 90 :
      average_grade = sum / tot_students
      grade_list = [average_grade]
      list_sum.extend(grade_list)
      print(list_sum)