


player_list = {1: 1, 2: 9, 3: 4}

sorted_times = sorted(player_list.values())
sorted_dict = {}

for i in sorted_times:
    for j in player_list.keys():
        if player_list[j] == i:
            sorted_dict[j] = player_list[j]
            break

print(sorted_dict)