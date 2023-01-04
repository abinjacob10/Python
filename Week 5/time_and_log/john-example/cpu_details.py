import psutil

def cpu_details():
  return (psutil.cpu_count(), psutil.cpu_percent())
