# this program converts floating numbers
# into base 2 ( binary ) numbers.
  

def to_bin(number, places = 3): 
  
    whole, dec = str(number).split(".") 

    if len(whole) == 0:
        whole = ("0")
    if len(dec) == 0:
        dec = ("0")
  
    whole = int(whole) 
    dec = int (dec) 
  
    res = bin(whole).lstrip("0b") + "."
  
    for x in range(places): 
  
        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
  
        dec = int(dec) 
  
        res += whole 
  
    return res 
  

def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return float(num) 
  

  
# Take the user input for  
# the floating point number 
n = input("Enter your floating point value : \n") 
  
# Take user input for the number of 
# decimal places user want result as 
p = int(input("Enter the number of decimal places of the result : \n")) 
  
print(to_bin(n, places = p)) 
