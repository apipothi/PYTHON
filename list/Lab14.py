print("****************List In PYTHON************************")
# Author : API POTHI
# URL    : https://www.youtube.com/apipothi
# TOPIC  : List with split() function
#Video   : 19
print("****************************************")

myWord_List="I LOVE API POTHI"
word_list=list(myWord_List.split())
print(word_list) # ['I', 'LOVE', 'API', 'POTHI']

print("------------------------------------")

myNumbers="1,2,3,4,5"

myList=myNumbers.split(',')
print(myList) # ['1', '2', '3', '4', '5']

print("------------------------------------")

sentenceWithDelimetr="Hello\tHow\tAre\tYou"
mySent=sentenceWithDelimetr.split("\t")
print(mySent) # ['Hello', 'How', 'Are', 'You']





