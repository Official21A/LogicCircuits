
number1 = input("Enter A >> ")
number2 = input("Enter B >> ")

if not "." in number1:
	number1 += "."
if not "." in number2:
	number2 += "."
	
temp1 = number1.split(".")
temp2 = number2.split(".")


number1_real = temp1[0]
number1_decimal = temp1[1]


number2_real = temp2[0]
number2_decimal = temp2[1]


a = len(number1_real)
b = len(number2_real)
extra = abs(a - b)

if a > b:
	number2_real = ("0" * extra) + number2_real
elif b > a:
	number1_real = ("0" * extra) + number1_real

list1 = [number1_real[i] for i in range(len(number1_real))]
list2 = [number2_real[i] for i in range(len(number2_real))]

a = len(number1_decimal)
b = len(number2_decimal)
extra = abs(a - b)

if a > b:
	number2_decimal = number2_decimal + ("0" * extra)
elif b > a:
	number1_decimal = number1_decimal + ("0" * extra)

list1.append(".")
list2.append(".")

list1 += [number1_decimal[i] for i in range(len(number1_decimal))]
list2 += [number2_decimal[i] for i in range(len(number2_decimal))]

flag = True

for x, y in zip(list1, list2):

	if x == "." or y == ".":
		continue

	x = int(x)
	y = int(y)

	if x > y:
		print("A_GT_B")
		flag = False
		break
	elif y > x:
		print("A_LT_B")
		flag = False
		break

if flag:
	print("A_EQ_B")