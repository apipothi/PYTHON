"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 18. String in-Build Method str.isdecimal()
Python  : 3.0
"""
print("**********START-String  isdecimal()  Example**********")
#21.
#str.isdecimal()

s1 = "ABC"
print("s1->")
print(s1.isdecimal()) # false

s2 = "123"
print("s2->")
print(s2.isdecimal()) # true

s3 = '123.456'
x = s3.isdecimal() # false
print("s3->")
print(x)

s4 = '1,234,567'
x = s4.isdecimal() #False
print("s4->")
print(x)

s5 = ''
x = s5.isdecimal() #False
print("s5->")
print(x)

s6 = '\u0661'
x = s6.isdecimal() #True
print("s6->")
print(x)

s7 = '\u0034' #True
x = s7.isdecimal() #True
print("s7->")
print(x)

#Vulgar Fraction One Third ⅓
s10 = '\u2153'
x = s10.isdecimal()
print("s10->")
print(x)

print("**********END-String  isdecimal()  Example**********")