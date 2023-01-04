# Function definition

def func1():
  """
  This my first function 
  """
  print("Good Morning!!!")


#Calling a function. notice, two things are gone, "def" keywork and ":"
func1()



#function2, gives remaining hours in a day, waits for an integer(hour). Note: Input keyword returns string not int/float. COnverstion is required.
#below, added type hint as well, "time:int" suggests that the passed argument is expected to be int,  "-> int" suggests that the function will return an int  
def func2(time: int) -> int:
  """
  Gives remainig time in a day.
  """
  return 24-time

print("What is the time now(enter only hour in 24 hr format)?")
#assignment and conversion to integer
time1_int=int(input())
#time1_int=int(time1)

rest_time=func2(time1_int)

print("Remaining time of the day:",rest_time)


#map(function, iterable) function,

def double_number(n: int)->int:
  """
   Simple function to double a number
  """
  return n+n
# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map
print(list(result))


#lambda  Comments:ONe time function  lambda arguments: expression
#using lamda to get body mass index(bmi) ratio
bmi = lambda weight, height: weight/(height*height)
print("Weight in kg:")
weight=float(input())
print("Height in meter:")
height=float(input())
print("Your BMI:{:.2f}".format(bmi(weight,height)))

#"global" keyword, allows locally scoped function variable values to be seen as globally
my_string = "global"
def my_function():
 global my_string
 print(f"At the moment, my_string is: {my_string}")
 my_string = "mangled!"
my_function()
print(f"Now the global value of my_string is: {my_string}")



### Exercise question
def find_num(number_list: list, number: int)->bool:
  for iterate_number in number_list:
    if iterate_number == number:
      return True
    else:
      pass
result = find_num([1,2,3,4,5,6,7,8,9], 9)
print(result)


### Exercise question 2, check if there is an even number in a list of numbers, return true if found, else return false
##Logic: Two loops are used. First loop takes values from user and stores in a list. Second loop checks each element in list for an even number. I have used .pop() method to take out each element from list.
list1 = []
print("Enter 5 numbers")

def even():                     #function definition
  for i in range(5):            #first for loop to get numbers and store in list1 
    list1.append(input())       
  for i in range(5):            #second loop to pop out items from list and check if it is even
    num = int(list1.pop())
    if (num %2 == 0):          #check if number is even
      return 1                 #if even found, return 0 and break from the second loop
      break
    else:                      
      pass                     #do nothing, keep going
  return 0                     #if even number not found, return 0 to the called function even()

print("Return:",even())


##Exercise question 3, Lambda fucntion to calculate volume of a cylinder
#cylider-volume=3.14*r*r*height
print("What is the radius of cylinder in cm?")
r=float(input())
print("What is the height of cylinder in cm?")
height=float(input())
volume = lambda r : 3.14*r*r*height

print("Volume of cylinder:{:.2f} cm³".format(volume(r)))

