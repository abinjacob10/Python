#Inheritance

#Base class
class base1:
  var1 = 10
  def method1(ok, x:int) -> int:   # instead of self I used "ok", self is not a "keyword" in Python, but recommended to avoid confusion.
    ok.y=x+5
    return ok.y
 
#Derived class
class derived1(base1):
  def method2(self):
    print("Hello from method2 in brother derived")



#derived class is instantiated
obj1 = derived1()
#method2 from derived class is called
obj1.method2()
#method1 from base class is called using object of derived class
returned1 = obj1.method1(2)
#printof above statement
print(returned1)
#class variable of "base class" is accessed.
print(obj1.var1)






#Class Overriding - Base class is overwritten
print("Inheritance overriding example")

class Bike:
  def __init__(self, bike_type:str):
    self.name1 = bike_type
  def introduce(self):
    print("Bike is {} bike".format(self.name1))

class Bike_gears(Bike):
  def introduce(self):
    print("BIke is fabulous")


obj2 = Bike_gears("road")  # treat that we have base class(with __init__ method and "introduce" method) + BIke_gears class itself, so __init__ method is part of this one bigger class, so __init__ is expeting its argument
#INtroduce method from base class "BIke" got "overridden" by derived class "Bike-gears" 
obj2.introduce()      #Prints IKe is fabulous"


print("Calling the base class function")
Bike.introduce(obj2)                    # calling the base class directly
print(obj2.name1)                       # accessing method variable from base class using derived class object obj2
