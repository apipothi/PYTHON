print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Aliasing
# Video   : 19
print("****************************************")

list1  = [ 10, 20, 30, 40, 50 ]
#list2  = [ 10, 20, 30, 40, 50 ]
list2  = list1

print(list1)
print(list2)

print(id(list1)) # 4309807872
print(id(list2)) # 4309807872

print("___________________________")
list1.append(500)

print(list1)
print(list2)








