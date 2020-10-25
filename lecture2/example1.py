cover_price = input('Enter your cover price: ')
cover_price = float(cover_price)
discount_version = cover_price - (cover_price * 40) / 100
total_copy = 60
shipping_costs = (total_copy - 1) * 0.75 + 3
total_costs = (float(discount_version) * 60 ) + float(shipping_costs)
print(total_costs)80