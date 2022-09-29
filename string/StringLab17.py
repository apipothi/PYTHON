"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 17. String in-Build Method center(),count(),encode(),endswith()
Video   : 17
Python  : 3.0
Documentation : https://docs.python.org/3/library/codecs.html#standard-encodings
"""
inputStringEncoding="pythön!"

print("****************center()***************")
inputStringCenter="APIPOTHI"
outputStringCenter=inputStringCenter.center(10)
print(outputStringCenter)

inputStringCenter1="APIPOTHI"
outputStringCenter1=inputStringCenter1.center(20,"*")
print(outputStringCenter1)
print(len("******APIPOTHI******"))

print("****************count()***************")
inputStringCount="API POTHI API POTHI TALK Education TALK"

outputStringCount=inputStringCount.count("POTHI")
print(outputStringCount)

outputStringCount=inputStringCount.count("API")
print(outputStringCount)

outputStringCount=inputStringCount.count("Education")
print(outputStringCount)

inputStringCount1="API POTHI API POTHI TALK is an Education TALK launched by API POTHI TEAM API POTHI"
outputStringCount1=inputStringCount1.count("POTHI",10,len(inputStringCount1))
print(outputStringCount1)

print("****************encode()***************")
inputStringEncode="APIPOTHI"
outputStringEncode=inputStringEncode.encode()
print(outputStringEncode)

inputStringEncoding="pythön!"
outputStringEncode1=inputStringEncoding.encode()
print(outputStringEncode1)


inputStringEncoding="pythön!"
outputStringEncode2=inputStringEncoding.encode("shift_jisx0213")
print(outputStringEncode2)

inputStringEncoding="pythön!"
outputStringEncode3=inputStringEncoding.encode("shift_jisx0213")
print(outputStringEncode3)

inputStringEncoding="pythön!"
outputStringEncode4=inputStringEncoding.encode("shift_jisx0213","strict")
print(outputStringEncode4)

print("****************endswith()***************")

inputStringEndswith="API POTHI."
outputStringEndswith=inputStringEndswith.endswith(".")
print(outputStringEndswith)

inputStringEndswith1="API POTHI API TALK."
outputStringEndswith1=inputStringEndswith1.endswith("TALK")
print(outputStringEndswith1)

inputStringEndswith2="API POTHI API TALK"
outputStringEndswith2=inputStringEndswith2.endswith("TALK")
print(outputStringEndswith2)


inputStringEndswith3="API POTHI API TALK API POTHI TALK"
outputStringEndswith3=inputStringEndswith3.endswith("TALK",3,len(inputStringEndswith3))
print(outputStringEndswith3)