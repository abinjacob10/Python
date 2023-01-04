a=10
b=20

if not a==b:
 print("ok")
else:
 print("not ok")

numerator = 30
denominator = 5
result = numerator % denominator == 0

print("result:",result)

def divisible(numerator: int, denominator: int) -> bool:
  return numerator % denominator == 0
print(divisible(30,5))
