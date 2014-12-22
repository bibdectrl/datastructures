from stack import Stack

def div_by_two(dec_num):
    numstack = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        numstack.push(rem)
        dec_num = dec_num // 2

    binString = ""
    while not numstack.isEmpty():
        binString += str(numstack.pop())
    return binString

def base_converter(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numstack = Stack()
    while num > 0:
        rem = num % base
        numstack.push(rem)
        num = num // base
    numstring = ""    
    while not numstack.isEmpty():
        numstring += digits[numstack.pop()]
    return numstring


print div_by_two(1)
print div_by_two(2)
print div_by_two(8)
print div_by_two(16)
print div_by_two(48)
print div_by_two(69)

print base_converter(26, 26)
