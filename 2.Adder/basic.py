# this program, gets two numbers in binary format and then 
# compares them, just like the circuits in your system do.

from binary import to_bin
import sys

if len(sys.argv) == 3:
	# command input for testbench
	number1 = sys.argv[1]
	number2 = sys.argv[2]
else:
	# numbers_input
	number1 = input("Enter A >> ")
	number2 = input("Enter B >> ")

# add float part
if not "." in number1:
	number1 += "."
if not "." in number2:
	number2 += "."

number1 = to_bin(number1)
number2 = to_bin(number2)

# seperate the float part from real part	
temp1 = number1.split(".")
temp2 = number2.split(".")


number1_real = temp1[0]
number1_float = temp1[1]

number2_real = temp2[0]
number2_float = temp2[1]


# modify the real part
a = len(number1_real)
b = len(number2_real)
extra = abs(a - b)

if a > b:
	number2_real = ("0" * extra) + number2_real
elif b > a:
	number1_real = ("0" * extra) + number1_real

list1 = [number1_real[i] for i in range(len(number1_real))]
list2 = [number2_real[i] for i in range(len(number2_real))]

# modify the float part
a = len(number1_float)
b = len(number2_float)
extra = abs(a - b)

if a > b:
	number2_float = number2_float + ("0" * extra)
elif b > a:
	number1_float = number1_float + ("0" * extra)

list1.append(".")
list2.append(".")

list1 += [number1_float[i] for i in range(len(number1_float))]
list2 += [number2_float[i] for i in range(len(number2_float))]

# next we iterate throught numbers parts to compare theme
flag = True
carry_out = 0
output = []
for i in range(len(list1)-1,-1):

	if list1[i] == ".":
		output.append(".")
		continue

	x = int(list1[i])
	y = int(list2[i])

	xyxor = xor_gate(x,y)
	xyand = and_gate(x,y)

	s = xor_gate(carry_out, xyxor)
	c = or_gate(xyand, and_gate(carry_out, xyand))

	output.append(str(s))

	if (i + 1 == len(list1)):
		if c == carry_out:
			print(">> valid")
		else:
			print(">> overflow")

	carry_out = c

print(reverse(output), sep="")