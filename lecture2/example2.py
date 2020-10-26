#A book club promises to send 8 books for $1 each, if you join the club. After you receive the first 8 books, you may select more books at a rate of $19.99 per book. If you spend a total of $80.96, how many extra books did you purchase?
spent = 80.96
first_join_books_number = 8
first_join_books_spent = first_join_books_number * 1
extra_books_number = (spent - first_join_books_spent) / 19.99
extra_books_number = int(extra_books_number)
print(extra_books_number)