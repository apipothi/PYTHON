"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : Slicing in Python
Video   : 13
Python  : 3.0
"""

print("********Slice in Python String*********")
#POSITEVE Indexing
   # A   B   C   D   E   F   G   H   I
   # 0,  1,  2,  3,  4,  5,  6,  7,  8
myYoutubeChannel = "ABCDEFGHI"
#[Start Index : End Index-1]
#[Lower Bouend : Upper Bound]

print("[2:7]"+myYoutubeChannel[2:7])#CDEFG
print("[0:0]"+myYoutubeChannel[0:0])#
print("[0:100]"+myYoutubeChannel[0:100])#ABCDEFG
print("[50:100]"+myYoutubeChannel[50:100])#
print("[0:5]"+myYoutubeChannel[0:5])# A   B   C   D   E
print("[:5]"+myYoutubeChannel[:5])# A   B   C   D
print("[2:0]"+myYoutubeChannel[2:0])#
print("[2:]"+myYoutubeChannel[2:])#C   D   E   F   G   H   I


print("Negative Index Slicing")

#Negative Indexing
myYoutubeChannel = "ABCDEFGHI"
   # A   B   C   D   E   F   G   H   I
   #-9, -8, -7, -6, -5, -4, -3, -2, -1
print("[-0:-0]"+myYoutubeChannel[-0:-0])
print("[-1:-0]"+myYoutubeChannel[-1:-0])
print("[-1:-1]"+myYoutubeChannel[-1:-1])

#-7<-1

print("[-7:]"+myYoutubeChannel[-7:])#C   D   E   F   G   H   I
print("[:-3]"+myYoutubeChannel[:-3])# A   B   C   D   E   F

#Upper Index>Lower Index
#-8>-2 - False
print("[-8:-2]"+myYoutubeChannel[-8:-2])#B   C   D   E   F   G
print("[-2:-8]"+myYoutubeChannel[-2:-8])#Wrong Argument


print("[::-1]"+myYoutubeChannel[::-1])#IHGFEDCBA
print("[::-2]"+myYoutubeChannel[::-2])#IGECA
print("[::-3]"+myYoutubeChannel[::-3])#IFC

print("[::-3]"+myYoutubeChannel[-1::-3])#IFC
print("[::-3]"+myYoutubeChannel[-2::-1])#HGFEDCBA