"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : For Loop in String
Video   : 11
Python  : 3.0
"""
print("***********How to Iterate the String*********")

myStringLoop1="API POTHI"
for loopvariable in myStringLoop1:
    print(loopvariable)#A P I  P

myStringLoop2="123456"
for loopvariable in myStringLoop2:
    print(loopvariable)


#in
print("String in Example")
myStringLoop3="API POTHI"
print("API" in myStringLoop3)

myStringLoop4="API POTHI"
print("TALK" in myStringLoop4)

myStringLoop5="API POTHI"
print("H" in myStringLoop5)

#if
print("String if Example")
myStringLoop6="API POTHI"
if "API" in myStringLoop6:
    print("API EXIST")

    myStringLoop7 = "API POTHI"
    if "APD" in myStringLoop7:
        print("API EXIST")

myStringLoop8 = "API POTHI"
if "APD" in myStringLoop8:
    print("APD EXIST")
else:
    print("APD Not Exist")

#not
print("String Not Example")

myStringLoop9="API POTHI"
if "APID" not in myStringLoop9:
    print("APID not Exist")
else:
    print("APID Exist")

if "API" not in myStringLoop9:
    print("API not Exist")
else:
    print("API Exist")