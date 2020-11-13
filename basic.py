
number1 = input("Enter A >> ")
number2 = input("Enter B >> ")

list1 = number1.split(sep=None)
list2 = number2.split(sep=None)

flag = True

for x, y in zip(list1, list2):
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