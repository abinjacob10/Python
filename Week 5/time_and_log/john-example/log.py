'''
Program shows utiliy to save log file based on datetime module


'''

from datetime import datetime as dt




time1 = dt.now()
print("printin year {}".format(time1.year))
# Linux
file_name = '%d-%d-%d-%d-%d-%d' % (time1.year, time1.month, time1.day, time1.hour, time1.minute, time1.second)



print(file_name)


#if(__name__ == "__main__"):
#  print('/home/pi/logfiles/' + file_name)
