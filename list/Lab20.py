print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Using Slice Operator
#Video   : 19
print("****************************************")

# -Ve   =  -5,  -4, -3, -2, -1
# List  = [ 10, 20, 30, 40, 50 ]
# +Ve   =   0,   1,  2,  3,  4

list  = [ 10, 20, 30, 40, 50 ]
print(list) # [10, 20, 30, 40, 50]
print("------- Slice() Using -Ve Index -------")
print("[-0:-0]",list[-0:-0]) # []
print("[-1:-0]",list[-1:-0]) # []
print("[-1:-1]",list[-1:-1]) # []
print("[-1:-4]",list[-1:-4]) # []

print("[-4:-2]",list[-4:-2]) # [20,30]
print("[-4:-1]",list[-4:-1]) # [20,30, 40]










