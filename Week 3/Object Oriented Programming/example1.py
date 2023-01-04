	## Class Attriubute reference

class class1:
  """This is an example CLass"""
  i=10
  def class_func1(self):
    return "hello Letterkenny"

print(class1.i)
print(class1.class_func1)
print(class1.__doc__)


## Class instantiation
class class2:
  def __init__(self,a1,a2):
    self.x=a1
    self.y=a2
    print("DOnegal gals are the most beautiful gals")
object1 = class2(3,4)
#object1.x and object1.y is also called "data attribute" instance object
print(object1.x,object1.y)





## MEthod objects

class class3:
  def f1(self):
    return 'Letterkenny'

#Class instantiation
object3 = class3()
# below, method f1 is called using object3
print(object3.f1())
print(type(class3.f1(object3)))

#below "method object" is stored in c, c could be used later to access the method f1.
c=object3.f1
#using c to access method f1
print(c())


## Class variable and instance variable

# Class variable is shared by all instances
# INstance variables are unique to each instance.


# Class variable, below gentle is shared by both class instances object2 and object3, object2.ways and object3.ways both print "gentle"
class Ireland:

  ways = 'gentle'

  def __init__(self, community):
    self.feature1 = community               # is unique to each instance
  def vegetation(self, test):
    self.f=test                             # is unique to each instance
    return self.f

#object1 = __init__("helpful")
object2 = Ireland("helpful")
object3 = Ireland("hard at work, fun in life")
c=object3.vegetation("not cropped")

# Below two outputs are same, class variable
print(object2.ways)
print(object3.ways)

print(object2.feature1)
print(object3.vegetation("not cropped"))
