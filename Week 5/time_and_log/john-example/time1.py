# Program explains about usage of "datetime" module

#IMporting object "datetime" from module  "datetime"
from datetime import datetime as dt
from datetime import timedelta as delta1

#calling method now() using datetime object, gives current local system, time
x=dt.now()
print(x)

#UNIX style output , needs time as argument
print(dt.timestamp(x))


#Based on format gives output, %A means week, gives the current week which is Sunday
#print(x.strftime("%A"))

def timestamp(extention):
  #Hours , miutes and seconds
#  timestamp1"{}:{}:{}".format(x.strftime("%H"), x.strftime("%M"), x.strftime("%S")))

  #Year:month:date || Hour :minute: seconds
  timestamp1 = "{}:{}:{}:{}:{}:{}".format(x.strftime("%Y"), x.strftime("%b"), x.strftime("%d"), x.strftime("%H"), x.strftime("%M"), x.strftime("%S"))
  
  return (timestamp1 + extention)
