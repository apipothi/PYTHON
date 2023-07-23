print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Cloning
# Video   : 19
print("****************************************")

list1  = [ 10, 20, 30, 40, 50 ]

list2  = list1.copy()

print(list1)
print(list2)

print(id(list1)) # 4308775680
print(id(list2)) # 4310465344

print("___________________________")
list1.append(600)

print(list1)
print(list2)






