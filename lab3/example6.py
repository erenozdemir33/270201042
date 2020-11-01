print("Quadratic function : (a * x^2) + b*x + c")
a = int(input('Enter the a parameter'))
b = int(input('Enter the b parameter'))
c = int(input('Enter the c parameter'))
r = (b ** 2) - 4 * (a * c)
if r > 0 : 
  x1 = (-b + r ** 0.5) / 2 * a
  x2 = (-b - r ** 0.5) / 2 * a
  print('There are 2 roots' , (x1 , x2))
elif r == 0 :
  x3 = -b / 2 * a
  print('There is 1 root' , x3)
elif r < 0 :
  print('No roots because discriminant < 0')
