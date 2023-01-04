
'''
The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. 
This is important because the default behavior for binding is to search the local namespace first. 
'''

spam=10

def outer_func():
  def local1():
    spam=20
  def local2():
    #below definition allows spam variable to refer to previously bound variable, which is spam=15
    nonlocal spam
    #now spam's value is changed from spam=15 to spam=30
    spam=30
  def local3():
    spam=40
  #as soon as local3()'s scope gets over, namespace associated also gets deleted, spam=40 is no more !! at this point



  
  spam=15
  local1()
  print("after local1() call",spam)
  local2()
  print("after local2() call", spam)
  local3()
  print("after local3() call", spam)
outer_func()
print("After completion of outer_func call", spam)
