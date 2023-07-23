print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : iter()
# Video   : 19
print("****************************************")

numbers= [1,2,3,4,5,6,7,8,9,10]

myItr=iter(numbers)
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #
print(next(myItr)) #

print("-------------------------------")

numbers1= [1,2,3,4,5,6,7,8,9,10]
length= len(numbers1)
myItr1=iter(numbers1)

print("------------------------------")
for i in range(0,length):
    print(next(myItr1))
