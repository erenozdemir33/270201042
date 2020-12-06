#numbers1 = [2,3,4,20,5,5,15]numbers2 = [10,20,20,15,30,40]●Convert these lists into the sets.●Intersection of the sets (without intersection operation)○Find and print the intersection of two sets●Union of the sets  (without union operation)●Find and print the union of the two sets.

numbers1 = [2,3,4,20,5,5,15]

numbers2 = [10,20,20,15,30,40]

numbers1 = set(numbers1)
numbers2 = set(numbers2)

intersection_x_y = {}
intersection_x_y = set(intersection_x_y)
for x in numbers1 :
  for y in numbers2 :
    if x == y :
      intersection_x_y.add(x)
      print(intersection_x_y)

numbers1 = list(numbers1)
numbers2 = list(numbers2)


numbers1.extend(numbers2)
print(set(numbers1))

