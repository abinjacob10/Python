
from time import sleep
from cpu_details import cpu_details
from time1 import timestamp 

logfile1=timestamp(".csv")
i=3

while i<10:
  sleep(1)
  if(i==10):
    exit(0)
  else:
    
#cpu-details collected, this will be shown at the end of each line of logfile1
    information = cpu_details()
#timestamp for each logline
    stamp1 = timestamp("")
#edited lines with (time+ cpu) details
    linex = stamp1 + "||" + str(information[0]) + "," + str(information[1]) + "\n"
    try:
      with open(logfile1, 'a') as f1:
        f1.write(linex)
    except:
      print("Error!!!")
    i=i+1
