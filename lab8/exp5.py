
def password_security_level_controler(password):
  numeric = []
  alphabetic = []
  special_characters = []
  level = 0


  for i in password :
    if i.isspace() == True or len(password) < 8 :
      return 0
    if i.isnumeric() == True :
      numeric.append(i)
    if i.isalpha() == True :
      alphabetic.append(i)
    if i.isalnum() == False and i.isspace() == False :
      special_characters.append(i)

  if len(numeric) > 0 :
    level += 1
  if len(alphabetic) > 0 :
    level += 1
  if len(special_characters) > 0 :
    level += 1
  
  return level

level = password_security_level_controler("asdadfaava152--  ")
print(level)

