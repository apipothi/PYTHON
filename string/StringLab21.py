"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 18. String in-Build Method str.isnumeric()
Python  : 3.0
"""
print("**********START-String  isnumeric() Example**********")

s1 = "ABC"
print("s1->")
print(s1.isnumeric()) # false

s2 = "123"
print("s2->")
print(s2.isnumeric()) # true

s3 = '123.456'
print("s3->")
x = s3.isnumeric() # false
print(x)

s4 = '1,234,567'
print("s4->")
x = s4.isnumeric() #False
print(x)

s5 = ''
print("s5->")
x = s5.isnumeric() #False
print(x)

s6 = '\u0661'
print("s6->")
x = s6.isnumeric() #True
print(x)

s7 = '\u0034'
print("s7->")
x = s7.isnumeric() #True
print(x)

s8 = '10²'
print("s8->")
x = s8.isnumeric()  #True
print(x)

s9 = '\u2465' # Special Unicode ⑥
x = s9.isnumeric()    #True
print("s9->")
print(x)

#Vulgar Fraction One Third ⅓
s10 = '\u2153'
x = s10.isnumeric()
print("s10->")
print(x)
# Prints True

print("**********END-String  isnumeric() Example**********")

