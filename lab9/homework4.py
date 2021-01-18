def Check2(num):
  if (num % 2 == 1):
    print(num)
    Check2(num + 1)

Check2(1)