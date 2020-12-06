equation1 = str(input("Enter your first equation : "))
equation2 = str(input("Enter your second equation : "))
#iki tarafa ayırdık denklemi
sp_equation1 = equation1.split("=")
#sağ sol olarak tanımladık
left_sp_equation1 = sp_equation1[0]

# + ların ve - lerin pozisyonunu blduk. ilk denklemin solu için
positions = []
for i in range(len(left_sp_equation1)):
    if left_sp_equation1[i] == "+" or left_sp_equation1[i] == "-":
        positions.append(i)

positions.append(len(left_sp_equation1))

split_left_equation1 = []
for index in range(len(positions) - 1):
    item = [left_sp_equation1[(positions[index]):(positions[index + 1])]]
    split_left_equation1.extend(item)

# termler split_left_equation1 olarak bulundu.
sum_numericfl = 0
sum_xfl = 0
sum_yfl = 0
for item in split_left_equation1:
    if "x" in item:
        position_x = item.index("x")
        x_count = item[0:(position_x)]
        sum_xfl = sum_xfl + int(x_count)
    elif "y" in item:
        position_y = item.index("y")
        y_count = item[0:(position_y)]
        sum_yfl = sum_yfl + int(y_count)
    else:
        int_value = int(item)
        sum_numericfl = sum_numericfl + int_value

right_sp_equation1 = sp_equation1[1]

positions = []
for i in range(len(right_sp_equation1)):
    if right_sp_equation1[i] == "+" or right_sp_equation1[i] == "-":
        positions.append(i)
positions.append(len(right_sp_equation1))

split_right_equation1 = []
for index in range(len(positions) - 1):
    item = [right_sp_equation1[(positions[index]):(positions[index + 1])]]
    split_right_equation1.extend(item)

sum_numericfr = 0
sum_xfr = 0
sum_yfr = 0
for item in split_right_equation1:
    if "x" in item:
        position_x = item.index("x")
        x_count = item[0:(position_x)]
        sum_xfr = sum_xfr + int(x_count)
    elif "y" in item:
        position_y = item.index("y")
        y_count = item[0:(position_y)]
        sum_yfr = sum_yfr + int(y_count)
    else:
        int_value = int(item)
        sum_numericfr = sum_numericfr + int_value

simplified_x_first = sum_xfl
if sum_xfr != 0:
    simplified_x_first = sum_xfl + (-1 * sum_xfr)

simplified_y_first = sum_yfl
if sum_yfr != 0:
    simplified_y_first = sum_yfl + (-1 * sum_yfr)

simplified_numeric_first = sum_numericfr
if sum_numericfl != 0:
    simplified_numeric_first = sum_numericfr + (-1 * sum_numericfl)

sp_equation2 = equation2.split("=")
left_sp_equation2 = sp_equation2[0]

positions = []
for i in range(len(left_sp_equation2)):
    if left_sp_equation2[i] == "+" or left_sp_equation2[i] == "-":
        positions.append(i)
positions.append(len(left_sp_equation2))

split_left_equation2 = []
for index in range(len(positions) - 1):
    item = [left_sp_equation2[(positions[index]):(positions[index + 1])]]
    split_left_equation2.extend(item)

sum_numeric_sl = 0
sum_x_sl = 0
sum_y_sl = 0
for item in split_left_equation2:
    if "x" in item:
        position_x = item.index("x")
        x_count = item[0:(position_x)]
        sum_x_sl = sum_x_sl + int(x_count)
    elif "y" in item:
        position_y = item.index("y")
        y_count = item[0:(position_y)]
        sum_y_sl = sum_y_sl + int(y_count)
    else:
        int_value = int(item)
        sum_numeric_sl = sum_numeric_sl + int_value

right_sp_equation2 = sp_equation2[1]
positions = []
for i in range(len(right_sp_equation2)):
    if right_sp_equation2[i] == "+" or right_sp_equation2[i] == "-":
        positions.append(i)
positions.append(len(right_sp_equation2))

split_right_equation2 = []
for index in range(len(positions) - 1):
    item = [right_sp_equation2[(positions[index]):(positions[index + 1])]]
    split_right_equation2.extend(item)

sum_numeric_sr = 0
sum_x_sr = 0
sum_y_sr = 0
for item in split_right_equation2:
    if "x" in item:
        position_x = item.index("x")
        x_count = item[0:(position_x)]
        sum_x_sr = sum_x_sr + int(x_count)
    elif "y" in item:
        position_y = item.index("y")
        y_count = item[0:(position_y)]
        sum_y_sr = sum_y_sr + int(y_count)
    else:
        int_value = int(item)
        sum_numeric_sr = sum_numeric_sr + int_value

simplified_x_second = sum_x_sl
if sum_x_sr != 0:
    simplified_x_second = sum_x_sl + (-1 * sum_x_sr)

simplified_y_second = sum_y_sl
if sum_y_sr != 0:
    simplified_y_second = sum_y_sl + (-1 * sum_y_sr)

simplified_numeric_second = sum_numeric_sr
if sum_numeric_sl != 0:
    simplified_numeric_second = sum_numeric_sr + (-1 * sum_numeric_sl)

print("Equations in the simplified form : ")
str_x = str(simplified_x_first) + 'x'
if simplified_x_first >= 0:
    str_x = '+' + str(simplified_x_first) + 'x'
str_y = str(simplified_y_first) + 'y'
if simplified_y_first >= 0:
    str_y = '+' + str(simplified_y_first) + 'y'
str_numeric = str(simplified_numeric_first)
if simplified_numeric_first >= 0:
    str_numeric = '+' + str(simplified_numeric_first)
print(str_x + str_y + "=" + str_numeric)

str_x = str(simplified_x_second) + 'x'
if simplified_x_second >= 0:
    str_x = '+' + str(simplified_x_second) + 'x'
str_y = str(simplified_y_second) + 'y'
if simplified_y_second >= 0:
    str_y = '+' + str(simplified_y_second) + 'y'
str_numeric = str(simplified_numeric_second)
if simplified_numeric_second > 0:
    str_numeric = '+' + str(simplified_numeric_second)
print(str_x + str_y + "=" + str_numeric)

x = 0
y = 0

a = simplified_x_first
b = simplified_y_first
c = simplified_numeric_first
d = simplified_x_second
e = simplified_y_second
f = simplified_numeric_second
x = 0
y = 0
if a == 0:
    y += c / b
    x += ((f) - ((e * c) / b)) / d
elif d == 0:
    y += f / e
    x += (c - ((b * f) / e)) / a
else:
    y += ((d * c) - (a * f)) / ((d * b) - (a * e))
    x += ((c) - (b * y)) / a

x = int(x)
y = int(y)

print("Solution :")
print("x = " + str(x))
print("y = " + str(y))