def binary_to_dec(binary_number) :

  decimal = 0
  for i in binary_number:
    print(i)
    decimal = decimal*2 + int(i)
  return decimal

decimal = binary_to_dec("10010")
print(decimal)



def dec_to_binary(decimal_number):

  if decimal_number > 1:
      dec_to_binary(decimal_number // 2)
  print(decimal_number % 2 , end="")

dec_to_binary(18)