"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 18. String in-Build Method expandtabs(),format_map(),isalpha(),isascii()
Video   : 18
Python  : 3.0
"""
import pdb
import sys

print("String expandtabs() Example")
inputExpandTab="Welcome\t to \t API\t POTHI\t PYTHON\t SERIES"
outputExpandTab=inputExpandTab.expandtabs()#8 sdpace
print(outputExpandTab)

inputExpandTab1="Welcome\t to \t API\t POTHI\t PYTHON\t SERIES"
outputExpandTab1=inputExpandTab1.expandtabs(20)#8 sdpace
print(outputExpandTab1)


print("String format_map() Example")
inptFormatMap={'a':"API POTHI",'b':"API POTHI TALK"}
inputMapString="Welcome to {a} & {b}"
outputFormatMap=inputMapString.format_map(inptFormatMap)
print(outputFormatMap)


print("String isalpha() Example")
inputIsAlpha="APIPOTHI"
outputIsAlpha=inputIsAlpha.isalpha()
print(outputIsAlpha)

inputIsAlpha1="API POTHI"
outputIsAlpha1=inputIsAlpha1.isalpha()
print(outputIsAlpha1)

inputIsAlpha2="APIPOTHI1"
outputIsAlpha2=inputIsAlpha2.isalpha()
print(outputIsAlpha2)

print("String isascii() Example")

inputIsAscii="API POTHI"
outputIsAscii=inputIsAscii.isascii()
print(outputIsAscii)

stringIsascii = "Åßõ"
outputIsAscii1=stringIsascii.isascii()
print(outputIsAscii1)