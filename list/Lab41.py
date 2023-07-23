print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : all()
# Video   : 19
print("****************************************")

list1  =  ['apple','banana','orange','cat']

result=all(list.startswith('a')  for list in list1)
print(result)

result1=all(list.startswith('z')  for list in list1)
print(result1)

result2=all(list.isdigit()  for list in list1)
print(result2)


print("-----------------------------------------")

myInteList=[2,4,6,8,10,12]
result3=all(myintlist % 2 == 0  for myintlist in myInteList)
print(result3)

myInteList1=[2,4,6,8,10,12,11]
result4=all(myintlist % 2 == 0  for myintlist in myInteList1)
print(result4) # False