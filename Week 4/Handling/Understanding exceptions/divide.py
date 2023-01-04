def divide(x,y):
  try:
    result =x/y
    print("End of try clause")
  except ZeroDivisionError:
    print("division by zero!") 
  else:
    print("result is:", result)
  finally:
    print("executing the finally clause")
divide(2,3)
divide(5,3)
divide(2,0)
divide('2','1')
