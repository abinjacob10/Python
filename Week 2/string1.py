

#String
a= "ATU Letterkenny"
b=" Donegal"

#String and number cannot be added together
print("a+b={}".format(a+b))
#print characters in reverse order
print(a[-1:-20:-1])
#print characters in ascending order
print(a[0:15:1])
#print the seventh character
print(a[7])
#print second word
print(a[4:])
#print first word
print(a[:2])

#Name=Abin, cannot change this string, but can use parts of it to make a new  name, below five lines changes Abin to Abun
name='Abin'
print(a)
first=name[0:2]
last=name[-1]
insert='u'
new=first+insert+last
print(new)

#string interpolation

string1=" how is it going Abin?"
print("31 days have passed in Letterkenny Ireland,"+ string1)

job_progress=3
sport=3

#formatting
print("job-progress={},sport={}".format(job_progress,sport))

#formatting using reference, format print order always depends on the order within {}
a="growing"
b="good"
#prints "growing good". 0th element is called first, and then 1st
print("Are you {0},{1} ?".format(a,b))
#prints "good growing", "second" element is called first and then "first"
print("Are you {second},{first} ?".format(second=b,first=a))


#formatted strings
print(f"{job_progress},{sport}")

#floating point formatting 
##using % operator
print("%0.3f"%(4/3))
##using format operator
print("{:.3f}".format(4/3))
##using f -string
print(f"{4/3:0.3f}")
print("%10f"%(4/3))
print("{:10f}".format(4/3))

##by default numbers are right justified
print("{:10.3f}".format(3/4))

##by default strings are left-alligned/left-justified
print("{:12}\r!!".format("Letterkenny"))

number=12.345
print("{:.2f}".format(number))

##f string or formatted string
print(f"{number}")

###about carriage return, takes the cursor back to the start of the same line. Below will print "okbye", because hello will be overwritten.

print("hello\rokbye")

###about line feeds(/n),python by default ends a line with /n. To suppress, use "end =", keyword as shown below
print("hello", end = "")
#multiline /n in single line
print("hello \n Letterkenny!!", end="")


#length of string
print("Length of a=",len(a))

#upper string
print("Upper of a=",a.upper())

#lower string
print("Lower of a=",a.lower())
