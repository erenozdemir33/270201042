
def is_prime(number) :
  count = 0
  for i in range(2,number):
    if number % i == 0 :
      count = count + 1
  if count != 0 :
    return False
  else :
    return True

prime_numbers = []
def print_primes_between(a,b) :
  for i in range(a+1,b) :
    if is_prime(i) == True :
      prime_numbers.append(i)
  print(prime_numbers)

a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

print_primes_between(a,b)



print(get_rand_list(0,10,5))
print(get_overlap())
    