print("****************Set In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Set In PYTHON
# VIDEO  : 20
print("****************************************")

my_Set={10,20,30,40}
try:
    my_Set.remove(200)
    print("My Actual Set", my_Set)
except KeyError as e:
    print("Error ::",e)


