str1 = input("Enter your word:")
str2 = input("Enter your word:")


def find_anagram_or_not(str1,str2) :
  if sorted(str1) == sorted(str2) :
    print("This words are anagram.")
  else :
    print("This words are not anagram")

find_anagram_or_not(str1,str2)