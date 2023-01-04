
import os, platform
current_working_directory = None

#This function return OS of the system in use
def detect_os() -> str:
  return platform.system()

#This function returns the present working directory.

def working_directory() -> str:
  return os.getcwd()


if(__name__ == '__main__'):
  print("This module is not imported")

  my_os=detect_os()
  print("My OS:",my_os)
  current_working_directory=working_directory()
  print(f"My Current working directory: {current_working_directory}")

else:
  print("__name__ is:",__name__)
  print("This module is imported and executed")
  my_os=detect_os()
  print("My OS:",my_os)
  current_working_directory=working_directory()
  print(f"My Current working directory: {current_working_directory}")

