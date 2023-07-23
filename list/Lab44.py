print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : filter()
# Video   : 19
print("****************************************")

def is_even(n):
    if(n%2==0):
        return True
    else:
        return False

numbers= [1,2,3,4,5,6,7,8,9,10]

even_Number=list(filter(is_even,numbers))
print(even_Number) # [2, 4, 6, 8, 10]

print("-------------------------------")

