 # leaveTime = 6.52
leave_time_minute = 6 * 60 + 52
passingTime_minute = (8 * 1) + (6 * 3) + (8 * 2)
arrivingTime_minute = (leave_time_minute + passingTime_minute) % 60
arrivingTime_hour = (leave_time_minute + passingTime_minute - arrivingTime_minute) / 60
arrivingTime = (int(arrivingTime_hour),arrivingTime_minute)
print(arrivingTime)