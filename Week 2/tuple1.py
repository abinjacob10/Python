
# A comma is compulasy to define a tuple, not a parenthesis. Parenthesis makes it moe clear
# reference: https://www.pythontutorial.net/python-basics/python-unpacking-tuple/
x=1,
print(type(x))
print(x)

a,c=1,2
print(a,c)

#swapping variable values using unpacking
#first, see how swapping works using tmp
tmp=a
a=c
c=tmp

print(a,c)

#using tuple unpacking, swapping two variables

a,c=c,a
print(a,c)


#using tuples to print multiple values
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
 print(a)
 print(b)
