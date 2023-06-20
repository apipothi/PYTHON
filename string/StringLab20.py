"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 18. String in-Build Method str.isdigit()
Python  : 3.0

"""
print("**********START-String  isdigit() Example**********")

s1 = "ABC"
print("s1->")
print(s1.isdigit()) # false

s2 = "123"
print("s2->")
print(s2.isdigit()) # true

s3 = '123.456'
print("s3->")
x = s3.isdigit() # false
print(x)

s4 = '1,234,567'
print("s4->")
x = s4.isdigit() #False
print(x)

s5 = ''
print("s5->")
x = s5.isdigit() #False
print(x)

s6 = '\u0661'
print("s6->")
x = s6.isdigit() #True
print(x)

s7 = '\u0034'
print("s7->")
x = s7.isdigit() #True
print(x)

s8 = '10²'
print("s8->")
x = s8.isdigit()  #True
print(x)

s9 = '\u2465' # Special Unicode ⑥
x = s9.isdigit()    #True
print("s9->")
print(x)
# Prints True

#Vulgar Fraction One Third ⅓
s10 = '\u2153'
x = s10.isdigit()
print("s10->")
print(x)
# Prints True
print("**********END-String  isdigit() Example**********")

