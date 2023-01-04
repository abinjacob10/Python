###About loops and statements
##if-elif-else
#in below example  only a is checked b and c are not checked.
a=1
b=0
c=0

if a:
  print("a is true")
elif b:
  print("b is true")
else:
  print("c is true")
#
a=0
b=0
c=0
if a:
  print("a is true")
elif b:
  print("b is true")
elif c:
  print("c is true")
else:
  print("logically all variables are false!!")

#logical AND,
#NOTE: "&&" and "AND" doesn't work, but "and" works

if (3<2) and (5<9):
  print("both conditions are true")
else:
  print("one codition is certainly false")

### for loop

#example1:prints every(x) value in beats.


beats = [1,2,3,4]


#below for loop statement "for x in beats", calls internal method __iter__ which helps in iteration
for x in beats:
#below indented code iterates through all elements of the list named beats. Prints elements(1,2,3,4) and prints each indexed item of list(1,2,3,4)
  print(x,beats[x-1])

#combining for and if
print("below output is modulus 2 of each of the elements in list named beats")
for y in beats:
#strange to me, comparison operators(==,!=,>,<,>=,<=) are accepted in Python but not conditional operators (||, !, &&)
  if(y%2 == 0):
   print(y)


#adding elements of a variable using for loop
expense=[23,9,3,45,7]
price=0
for x in expense:
 price+=x

print("price:",price)

#combining for and if loop, example 2
name="ATU Letterkenny"
for y in name:
 if(y == " "):
   print("space")

#using range() function, range(start,end,step)
for i in range(5,50,3):
  print(i)


#iterating dictionaries
#iterating technique "When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method."
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
  print("{}{:>5}{}".format(ipv4,"//",port))



###while loop


#list comprehension
list2=[]
string2="Cloud Operations"
for character in  string2:
  list2.append(character)
print(list2)


list3=[]
for number in range(20):
 list3.append(number)
print(list3)


my_list = [number * 10 for number in range(0,20)]
print(my_list)



# Exercise: CONverting kelvinf to degree and fahrenheit//FOrmulae C = K - 273  //F = 1.8(K - 273) + 32 
K=[-15,-5,-1,0,20,40,50,80,100,500]
C=[]
F=[]
for tempt in K:
  C.append(tempt-273)
#using above commented formula for fahrenheit conversion+ rounding the values.
  F.append(round(1.8*(tempt-273) + 32))
print("CElsius:",C)
print("Fahrenheit:",F)

