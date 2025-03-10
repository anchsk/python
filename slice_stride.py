str = "Hello, world!"

# Slice syntax: [start:stop]
print(str[1:2]) # e
print(str[:5]) # Hello 0,1,2,3,4
print(str[4]) # o 4th index, 5th character counting from 0
print(str[-1]) # ! last character
print(str[-3:-1]) # ld
print(str[-3:]) # ld!
# print(str[-100]) # IndexError: string index out of range # Python 3.12.2
# print(str[100]) # IndexError: string index out of range
print(str[100:]) # '' empty string

# Stride syntax: [start:stop:step]
print(str[::]) # Hello, world!
print(str[0:6:2]) # Hlo
print(str[:6:2]) # Hlo (from 0th index to 6th index, step 2)
print(str[7::2]) # wrd (from 7th index to end of string, step 2)
print(str[::3]) # Hl r! 0,3,6,9
print(str[::2]) # Hlo ol! 0,2,4,6,8,10
print(str[::-1]) # !dlrow ,olleH reverse string