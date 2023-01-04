#Different way to use list
y=[3,4,5]
print(y)
z=list([3,4,5])
print(z)

###LIsts, LISTS store different object types
list1=[1,1,1,3,"Hurling",4,"LK"]
print(list1)
#list-lenght
print(len(list1))
#list-indexing technique
slice1=list1[0:7:2]
print("slice1=",slice1)
print(list1[-1])
#concatenation of lists
list2=["skills","certification","projects in git","job"]
list3=list1+list2
print(list3)
#nested lists
list4=["sept","oct",list1]
print("list4",list4)
#editing individual elements in list
print(len(list4))

##List operations
#appending a list
list4.append("focus")
print(list4)
#inserting in a list
list4.insert(2,"think-before-act")
print("list4",list4)


##stack operatoions last-in-first-out
#pop
print("popped out",list4.pop())
#add an item to stack~append()
list4.append("focus")
print(list4)


###Tuple, data-structure same as lists, but are immutable. A comma is required to define a tuple
tuple1=(1,2,3,"32")
print(tuple1)

#changing 2nd element from int 3 to string "new"
#tuple1[2]=4
#below output in bold will fail
#print("new tuple:{}",tuple1)



###Dictionaries, unlike lists/tuples, in dictionaries data is arranged by key:value pair which are strings(?)

dict1={"key1":"time", "key2":"energy", "key3":"magic"}
print(dict1)

#editing a key:value pair
dict1["key3"]="grace"
print("new dictionary:",dict1)

print("this method gives keys:",dict1.keys())
print("this method gives values:",dict1.values())
print("this methis gives items:",dict1.items())


###SET, collection of unique objects

set1=set()
set1.add("three")
set1.add("one")
set1.add("three")
print(set1)
