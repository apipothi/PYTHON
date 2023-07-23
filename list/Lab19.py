print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : Using Slice Operator
#Video   : 19
print("****************************************")

# -Ve   =  -5,  -4, -3, -2, -1
# List  = [ 10, 20, 30, 40, 50 ]
# +Ve   =   0,   1,  2,  3,  4

#list[Start:End]
#list[M:N]
#list[M:N-1]

list  = [ 10, 20, 30, 40, 50 ]
print(list) # [10, 20, 30, 40, 50]
print("------- Slice() Using +Ve Index -------")
print("[0:0]",list[0:0]) #
print("[0:5]",list[0:5])   #  [ 10, 20, 30, 40, 50 ]
print("[0:50]",list[0:50]) #  [ 10, 20, 30, 40, 50 ]
print("[0:9]",list[0:9])   #  [ 10, 20, 30, 40, 50 ]
print("[:9]",list[:9])     #  [ 10, 20, 30, 40, 50 ]
print("[0:]",list[0:])     #  [ 10, 20, 30, 40, 50 ]
print("[:]",list[:])       #  [ 10, 20, 30, 40, 50 ]

print("[1:3]",list[1:3])       #  [20, 30]
print("[1:4]",list[1:4])       #  [20, 30, 40]





