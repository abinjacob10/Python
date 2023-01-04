
import os, platform
current_working_directory = None

#This function return OS of the system in use
def detect_os() -> str:
  return platform.system()

#This function returns the present working directory.

def working_directory() -> str:
  return os.getcwd()


#Create a directory with error handling
def create_directory(directory_name: str) ->bool:

  #check if directory already exists
  if os.path.isdir(directory_name):
    return 2

  else:
    try:
      # Create the diretory
      os.mkdir(directory_name)
      # If this worked, return True
      return True
    except:
      # Give an explicit error message
      print(f"Error creating directory {directory_name}")
      # If this did not work, return False
      return False


#__main__ , non __main__ block

if(__name__ == '__main__'):
  print("This module is not imported")
  my_os=detect_os()
  print("My OS:",my_os)
  current_working_directory=working_directory()
  print(f"My Current working directory: {current_working_directory}")
  
  #calls the create_directory function and checks if it was successfull
  if create_directory("AJ") == 1:
    print("Creating a directory worked")
  
  # Do other stuff
  elif create_directory("AJ") == 0:
    print("Error!!! You couldn't create a directory!")
  
  ## Waiting for return = 2
  else:
    print("Directory already exists")

else:
  print("__name__ is:",__name__)
  print("This module is imported and executed")
  my_os=detect_os()
  print("My OS:",my_os)
  current_working_directory=working_directory()
  print(f"My Current working directory: {current_working_directory}")

