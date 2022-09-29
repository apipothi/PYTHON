"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : 16. String in-Build Method replace(),split(),casefold(),capitalize()
Video   : 16
Python  : 3.0
"""
print("*********** replace() *********")
inputStringReplace="API POTHI YouTube"
outputStringReplace=inputStringReplace.replace("YouTube","TALK")
print(outputStringReplace)

inputStringReplace1="API POTHI API POTHI Talk API POTHI Youtube"
outputStringReplace1=inputStringReplace1.replace("API","TALK",3)
print(outputStringReplace1)

print("*********** split() *********")
inputStringSplit="API POTHI and API POTHI TALK are the PLAY LIST in our Youtube Channel"
outputStringSplit=inputStringSplit.split()
print(outputStringSplit)

inputStringSplit1="API POTHI and API POTHI TALK are the PLAY LIST in our Youtube Channel"
outputStringSplit1=inputStringSplit1.split(" ", len(inputStringSplit1))
print(outputStringSplit1)

inputStringSplit2="API,POTHI,and,API,POTHI,TALK,are,the,PLAY,LIST,in,our,Youtube,Channel"
outputStringSplit2=inputStringSplit2.split(",", len(inputStringSplit2))
print(outputStringSplit2)

print("*********** casefold() *********")
inputStringCasefold="API POTHI"
outputStringCasefold=inputStringCasefold.casefold()
print(outputStringCasefold)

inputStringCasefold1="api pothi"
outputStringCasefold1=inputStringCasefold1.casefold()
print(outputStringCasefold1)

print("****lower() Vs casefold()****")
specialString = "ΣςßêΊΦ"#σςßêίφ
print(specialString.lower())#σςßêίφ
print(specialString.casefold())#σσssêίφ

print("****capitalize()****")
inputStringCap="api pothi"#Api Pothi
outputStringCap=inputStringCap.capitalize()
print(outputStringCap)


inputStringCap1="api pothi talk"
outputStringCap1=inputStringCap1.capitalize()
print(outputStringCap1)

inputStringCap2="Api pothi talk"
outputStringCap2=inputStringCap2.capitalize()
print(outputStringCap2)