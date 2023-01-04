var0=0
def loc1():
 var1=1
 print("var1:",var1)
def loc2():
 var2=2
 var0=12
 print("var0:",var0)
var3=3
print("global var3:",var3)

loc2()

#In Local function spam(), an assignment is made after printing  
#Scenario 1
#FOllowing error is seen in Scenario 1 "UnboundLocalError: local variable 'eggs' referenced before assignment"


print("about eggs")

def spam():
  print(eggs) # ERROR!
  eggs = 'spam local'

eggs = 'global'
spam()
