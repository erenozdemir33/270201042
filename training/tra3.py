çitustaları= {}


while True :
  name = str(input("enter your usta name  if its done enter no"))
  if name == "no" :
    break
  tel_no = str(input("enter his phone if you write no pass this"))
  çitustaları.update({name:tel_no})
print(çitustaları)
