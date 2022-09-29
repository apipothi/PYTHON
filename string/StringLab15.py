"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 15. String in-Build Method len(),upper(),loweer(),strip()
Video   : 15
Python  : 3.0
"""
print("****************-15.String in-Build Method len(),upper(),loweer(),strip()-****************-")
print("****************-len()-****************-")

inputStringLen="APIPOTHI"
length=len(inputStringLen)

print(length)
inputStringLen1="         "
length1=len(inputStringLen1)
print(length1)

print("****************-upper()-****************-")
inputUpper="apipothi"
outputUpper=inputUpper.upper()
print(outputUpper)

inputUpper1="ApiPothi"
outputUpper1=inputUpper1.upper()
print(outputUpper1)

inputUpper2="APIPOTHI"
outputUpper2=inputUpper2.upper()
print(outputUpper2)

print("****************-lower()-****************-")

inputStringLower="APIPOTHI"
outputLower=inputStringLower.lower()
print(outputLower)

inputStringLower1="ApiPothi"
outputLower1=inputStringLower1.lower()
print(outputLower1)

inputStringLower2="apipothi"
outputLower2=inputStringLower2.lower()
print(outputLower2)

print("****************-strip()-****************-")
inputStrip="API APOTHI"
outputStrip=inputStrip.strip()
print(outputStrip)

inputStrip1="    API APOTHI     "
outputStrip1=inputStrip1.strip()
print(outputStrip1)

inputStrip2="    API APOTHI     "
outputStrip2=inputStrip2.strip(" ")
print(outputStrip2)

inputStrip3=",,,,....****((())))API APOTHI ,,,,....****((())))"
outputStrip3=inputStrip3.strip(",.*()")
print(outputStrip3)

print("****lower() Vs casefold()****")
specialString = "ΣςßêΊΦ"#σςßêίφ
print(specialString.lower())
print(specialString.casefold())