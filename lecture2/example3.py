#If I leave my house at 6:52 am and run 1 mile at an easy pace (8 minutes per mile), then 3 miles at tempo (6 minutes per mile) and 2 mile at easy pace again, what time do I get home for breakfast?
#leaveTime = 6.52
leave_time_minute = 6 * 60 + 52
passingTime_minute = (8 * 1) + (6 * 3) + (8 * 2)
arrivingTime_minute = (leave_time_minute + passingTime_minute) % 60
arrivingTime_hour = (leave_time_minute + passingTime_minute - arrivingTime_minute) / 60
arrivingTime = (int(arrivingTime_hour),arrivingTime_minute)
print(arrivingTime)