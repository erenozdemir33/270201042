month_name = str(input('Enter your month name'))
user_day = int(input('Enter your day'))
if user_day > 31 or user_day == 0 : 
  print('Not exist')
elif (month_name == 'January' or month_name == 'February' or month_name == 'December') or ( month_name == 'March' and user_day < 20) :
  print('WİNTER') 
elif (month_name == 'April' or month_name == 'May') or (month_name == 'March' and user_day >= 20) or (month_name == 'June' and user_day <= 21) :
  print('SPRİNG')
elif (month_name == 'June' and user_day >= 21) or (month_name == 'July' or month_name == 'August') or (month_name == 'September' and user_day < 22) :
  print('SUMMER')
else :
  print('FALL')March
  