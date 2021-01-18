#Write a recursive function that takes a string as input and returns the number of Write a recursive function that takes a string as input and returns the number of non-alphanumeric characters. Make a call to this function with "&1ac*b1 d-4!+" and print the output (It should print 6).. Make a call to this function with "&1ac*b1 d-4!+" and print the output (It should print 6)


def non_alphanumeric_characters_counter(string) :

  if len(string) == 0 :
    return 0
  else :
    count = 0
    if string[0].isalnum() == False :
      count += 1
    return count + non_alphanumeric_characters_counter(string[1:])

print(non_alphanumeric_characters_counter("&1ac*b1 d-4!+"))
