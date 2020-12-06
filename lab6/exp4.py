#Write a program that gets a list from the user and shows another list that contains only unique elements of the given list in a descending order.
user = input("Enter a list")
user = list(set(user))
print(user)