
def password_security_level_controler(password):
  level = 0
  for i in password :
    if i.isspace() == True or len(password) < 8 :
      return 0
    if i.isnumeric() == True :
      level += 1 
      pass
    if i.isalpha() == True :
      level += 1
      pass
    if i.isalnum() == False :
      level += 1
      pass
  return level

print(password_security_level_controler("asdadfaava152"))

