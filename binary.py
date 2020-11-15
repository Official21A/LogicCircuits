# this program converts floating numbers
# into base 2 ( binary ) numbers.
  

def to_bin(number, places=20): 
  
    real, dec = number.split(".") 

    if len(real) == 0:
        real = ("0")
    if len(dec) == 0:
        dec = ("0")
  
    real = int(real) 
    dec = int (dec) 
  
    res = bin(real).lstrip("0b") + "."
  
    for x in range(places): 
        real, dec = str((decimal_converter(dec)) * 2).split(".") 
        dec = int(dec) 
        res += real 
        
        if dec == 0:
            break
  
    return res 
  

def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return float(num) 
