province_file = open('provinces.txt')
province_dict = {}
while True:
  line = province_file.readline().strip("/n")
  if line == "":
    break
  province_names , latitude , longitude  = line.split(',')
  longitude = longitude.strip()
  province_dict[province_names] = latitude,longitude

province_file.close()

possible_departure_list = []
keys = province_dict.keys()

while True :
  departure_province = input("Departure province:\n")
  departure_province = departure_province.upper()
  if departure_province in keys:
    break

  if departure_province not in keys :
    for x in keys :
      if departure_province == x[:len(departure_province)] :
        possible_departure_list.append(x)
        possible_departure_list.sort()
    print("Province not found!")
    if len(possible_departure_list) != 0 :
      message = ("Possible province:")
      for index in range(len(possible_departure_list)):
        message = message + possible_departure_list[index]
        if index != len(possible_departure_list) - 1:
          message = message + ','
      print(message)
      possible_departure_list.clear()

possible_arrival_list = []

while True:
  arrival_province = input("Arrival province:\n")
  arrival_province = arrival_province.upper()
  if arrival_province in keys:
    break
  if arrival_province not in keys:
    for x in keys:
      if arrival_province == x[:len(arrival_province)]:
        possible_arrival_list.append(x)
    possible_arrival_list.sort()
    print("Province not found!")
    if len(possible_arrival_list) != 0 :
      print("Possible province:")
      message = ("Possible province:")
      for index in range(len(possible_arrival_list)):
        message = message + possible_arrival_list[index]
        if index != len(possible_arrival_list) - 1:
          message = message + ','
      print(message)
      possible_arrival_list.clear()
while True :
  if departure_province != arrival_province :
    break
  if departure_province == arrival_province :
    print("Enter a different province!")
    arrival_province = input("Enter your arrival province")

travel_type_list = ["CAR","MOTORCYCLE","BİCYCLE"]

while True :
  travel_type = input("Enter travel type:\n")
  travel_type = travel_type.upper()
  if travel_type in travel_type_list :
    break

speed = {
  "CAR" : 90,
  "BICYCLE" : 25,
  "MOTORCYCLE" : 80,
}

x1 = province_dict[departure_province][0]
x2 = province_dict[arrival_province][0]
y1 = province_dict[departure_province][1]
y2 = province_dict[arrival_province][1]

dx = float(x2) - float(x1)
dy = float(y2) - float(y1)

distance = ((dx * dx) + (dy * dy)) ** 0.5
distance = float(distance)
distance_km = distance * 100
distance_km = float(distance_km)
distance_km = round(distance_km, 2)


time = distance_km / speed[travel_type]


hours = int(time)
minutes = (time - hours) * 60
minutes = int(minutes)
print("\nI am calculating the distance between " + departure_province + " and " + arrival_province + " ...\n")
print("Distance: " + str(distance_km) + " km")
keys = province_dict.keys()

distance_dict = {}

for key , value in province_dict.items() :
  if key == departure_province :
    pass
  x1 = province_dict[departure_province][0]
  x2 = value[0]
  y1 = province_dict[departure_province][1]
  y2 = value[1]

  dx = float(x2) - float(x1)
  dy = float(y2) - float(y1)

  distance = ((dx * dx) + (dy * dy)) ** 0.5
  distance = float(distance)
  distance_km = distance * 100
  distance_km = float(distance_km)
  distance_km = round(distance_km, 2)
  distance_dict[key] = distance_km

sorted_distance = {}
for x in sorted(distance_dict, key=distance_dict.get):
  sorted_distance[x] = distance_dict[x]
sorted_distance = list(sorted_distance)

top_three = sorted_distance[1:4]
top_three.sort()

print("Approximate travel time with " + str(travel_type) + ": " + str(hours) + " hours " + str(minutes) + (" minutes"))
message = ("Recommended places close to ") + str(departure_province) + ":"
for index in range(len(top_three)):
  message = message + top_three[index]
  if index != len(top_three)-1:
    message = message + ','
print(message)
