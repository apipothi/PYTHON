print("****************Set In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Set In PYTHON
# VIDEO  : 20
print("****************************************")

my_Set=set()
my_Set.update({10,20,30,40})
print("My Actual Set",my_Set)

myList=[90,91,92,93]
my_Set.update(myList)
print("Set with List Element",my_Set)

myAnotherSet={22,33}
my_Set.update(myAnotherSet)
print("Set with Set Element",my_Set)