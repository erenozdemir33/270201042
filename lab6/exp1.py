#Ask for an email address.
#Check if this email address is ceng113@example.com
#Assume that (for this domain):
#mail addresses are case-insensitive 	(e.g. abc@def.com and ABC@DEF.com are the same address)
#Dots before @ sign are ignored	(e.g. a.b.c@def.com and abc@def.com are the same address)

user = str(input("Enter your e mail adress :"))
user_check = user.lower()
if (user != user_check) or ( user.count(".") != 1) :
  print("this is not true")
elif user == "ceng113@example.com" :
  print("welcome")
else :
  print("this is not true")
