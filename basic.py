
number1 = input("Enter A >> ")
number2 = input("Enter B >> ")

a = len(number1)
b = len(number2)
extra = abs(a - b)

if a > b:
	number2 = ("0" * extra) + number2
elif b > a:
	number1 = ("0" * extra) + number1

list1 = [number1[i] for i in range(len(number1))]
list2 = [number2[i] for i in range(len(number2))]


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