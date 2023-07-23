print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : List In PYTHON
#Video   : 19
print("****************************************")

myList=[1,2,3,4,5]
print(myList) # [1,2,3,4,5]

myEmpltyList=[]
print(type(myEmpltyList))
print("List Size :: ", len(myEmpltyList)) # 0
myEmpltyList.append(10)
myEmpltyList.append(11)
myEmpltyList.append(12)
myEmpltyList.append(13)
myEmpltyList.append(14)
print(type(myEmpltyList))
print("List Size :: ", len(myEmpltyList)) # 5

myEmpltyList.remove(13)
print(type(myEmpltyList))
print("List Size :: ", len(myEmpltyList)) # 5-1=4

