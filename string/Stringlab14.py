"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : Way to Find Index in Python -Find() ,rFind() ,index(), rindex()
Video   : 14
Python  : 3.0
"""
print("****************-Way to Find Index in Python-****************-")
print("****Find()****")
inputStringFind="API POTHI"
print(inputStringFind.find("API"))
inputStringFind1="API POTHI"
print(inputStringFind1.find("P"))
inputStringFind2="ABCDEFGHIABCAABC"
print(inputStringFind2.find("ABC",3,len(inputStringFind2)))
inputStringFind3="API POTHI"
print(inputStringFind3.find("XYZ"))

print("****rFind()****")
inputStringrFind="API POTHI API POTHI"
print(inputStringrFind.rfind("API"))
inputStringrFind="API POTHI API POTHI"
print(inputStringrFind.rfind("A"))
inputStringrFind="API POTHI API POTHI"
print(inputStringrFind.rfind("I"))
print(len(inputStringrFind))
inputStringrFind1="API POTHI API POTHI"
print(inputStringrFind1.rfind("API",4,len(inputStringrFind1)))
inputStringrFind2="API POTHI API POTHI"
print(inputStringrFind2.rfind("XYZ"))

print("****index()****")
inputStringrIndex1="API POTHI API POTHI"
print(inputStringrIndex1.index("API"))
inputStringrIndex2="API POTHI API POTHI"
print(inputStringrIndex2.index("A"))
inputStringrIndex3="APIPOTHI XYZ APIPOTHI"
print(inputStringrIndex3.index("API",3,len(inputStringrIndex3)))
inputStringrIndex4="APIPOTHI XYZ APIPOTHI"
#print(inputStringrIndex4.index("LKM"))


print("****rindex()****")
inputStringrrIndex1="API POTHI API POTHI"
print(inputStringrrIndex1.rindex("API"))
inputStringrrIndex2="API POTHI API POTHI"
print(inputStringrrIndex2.rindex("A"))
inputStringrrIndex3="APIPOTHI XYZ APIPOTHI"
print(inputStringrrIndex3.rindex("API",3,len(inputStringrrIndex3)))
inputStringrrIndex4="APIPOTHI XYZ APIPOTHI"
#print(inputStringrrIndex4.rindex("LKM"))