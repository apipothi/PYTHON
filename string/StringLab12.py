"""
Author  : API POTHI
YouTube : www.youtube.com/c/APIPOTHI
Topic   : String Formatting in Python
Video   : 12
Python  : 3.0
"""
print("***********String Formatting in Python*********")
print("*********** formatted string literals *********")
#API POTHI have Python playlist which conatain 13 video
print("API POTHI have Python playlist which conatain 13 videos")

print('%(channelName)s have %(language)s playlist which conatain %(videos)d videos'
      %{"channelName":'API POTHI',"language":"Python","videos":13})

#f-String
channelName= 'API POTHI'
language="Python"
videos= 13
print(f"{channelName} have {language} playlist which conatain {videos} videos" )

print("*********** template strings *********")
#API POTHI Channel have total 149 Videos
totalVideos=149
infoString="API POTHI Channel have total {} Videos"
print(infoString.format(totalVideos))

totalVideos=149
infoString="API POTHI Channel have total {:.2f} Videos"
print(infoString.format(totalVideos))


#API POTHI got 10K Subscriber along with 149 videos
aboutApipothi="{channelName} got {subscriber}K Subscriber along with {videos} videos"
print(aboutApipothi.format(channelName="APIPOTHI",subscriber=10,videos=149))

channelName="APIPOTHI"
subscriber=10
videos=149

aboutApipothi="{} got {}K Subscriber along with {} videos"
print(aboutApipothi.format(channelName,subscriber,videos))

channelName="APIPOTHI"
subscriber=10
videos=149

aboutApipothi="{0} got {2}K Subscriber along with {1} videos"
print(aboutApipothi.format(channelName,videos,subscriber))

channelName="APIPOTHI"
subscriber=10
videos=149

aboutApipothi="{0} got {1}K Subscriber along with {2} videos1"
print(aboutApipothi.format(subscriber,videos,channelName))

piValue=22/7
print(piValue)
print("Value of pi is {pi}".format(pi=piValue))
print("Value of pi is  {pi:1.3f}".format(pi=piValue))