file_name = input("enter your file name")
user_file = open(file_name,encoding="utf-8")

diction = {}
word_list = []
while True:

  letter = input("enter a one or more letter operator if you done enter quit")
  if letter == "quit":
    break
  while True :
    line = user_file.readline()
    if line == "":
      break
    for x in range(len(letter)) :
      i = letter[x]
      for word in user_file.read().split():
        if i in word:
          word_list.append(word)
          biggest_len = 0
          for a in word_list :
            if len(a) > biggest_len :
              biggest_len = len(a)
              biggest = a
              diction[i] = a
print(diction)

               
     













    name, email = line.split(':')
    member_dict3[name] = email[1:].split('\n')[0]
    line = member_file.readline()