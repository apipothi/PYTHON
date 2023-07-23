print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : any()
# Video   : 19
print("****************************************")
list1  =  ['apple','banana','orange','cat']

result=any(list.startswith('a')  for list in list1)
print(result)


result1=any(list.startswith('z')  for list in list1)
print(result1)


result2=any(list.isdigit()  for list in list1)
print(result2)





