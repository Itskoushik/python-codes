# n=int(input("enter the number of sq matrix: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 and j==3 or i==2 and j in (2,3) or i==3 and j in (2,3,4):
#             print("*"+"  ",end=" ")    
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character



#functions
#they are set of block of code which are meant to perform specific tasks.
#advantages of using functions.
#it reduces the instructions (code redundancy)
#it reduces code repeatition and also reduces the time consumed by programmers and also reduces the code length
#it improves code reuseability 
#there are 2 types of functions.
'''
inbuilt functions and user defined functions.

inbuilt functions:
these are prefined functions which are written by developers which are meant to perform certain tasks.

user defined functions:
these are the functions written by users to improve code reuseability and reduce lines of code
'''
#dir() used to retrieve all the functions on the specific datatype in a list
#example: dir(list)

# methods on string
'''
inbuilt functions:

islower(): it is a function which returns true/false if all the alphabets are lowercase .
#note it ignores digits,whitespaces and special characters 

isupper():it is a function which returns true/false if all the alphabets are uppercase .
#note it ignores digits,whitespaces and special characters

isdigit():it is a function which returns true/false if all the characters are digit .
isalpha(): Returns True if all characters in the string are in the alphabet
isalnum():	Returns True if all characters in the string are alphanumeric
join():	Joins the elements of an iterable to the end of the string
startswith():	Returns true if the string starts with the specified value
endswith()	Returns true if the string ends with the specified value
lower():	Converts a string into lower case
upper():	Converts a string into upper case
strip():	Returns a trimmed version of the string
lstrip():	Returns a left trim version of the string
rstrip():	Returns a right trim version of the string
swapcase():	Swaps cases, lower case becomes upper case and vice versa 
count():	Returns the number of times a specified value occurs in a string
find():	Searches the string for a specified value and returns the position of where it was found
index():	Searches the string for a specified value and returns the position of where it was found

#extra methods
replace():	Returns a string where a specified value is replaced with a specified value
isspace():	Returns True if all characters in the string are whitespaces


'''

#methods on list:
'''
append():	Adds an element at the end of the list
clear():	Removes all the elements from the list
copy():	Returns a copy of the list
count():	Returns the number of elements with the specified value
extend():	Add the elements of a list (or any iterable), to the end of the current list
index():Returns the index of the first element with the specified value
insert():	Adds an element at the specified position
pop():	Removes the element at the specified position
remove():	Removes the item with the specified value
reverse():	Reverses the order of the list
sort():	Sorts the list


'''
s=[]

#methods on tuple:
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found


'''
#methods on set:
'''
Method	          Shortcut	            Description
add()	 	                    Adds an element to the set
clear()	 	                    Removes all the elements from the set
copy()	 	                    Returns a copy of the set
difference()	     -	        Returns a set containing the difference between two or more sets
difference_update()  -=	        Removes the items in this set that are also included in another, specified set
discard()	 	                Remove the specified item
intersection()	      &	        Returns a set, that is the intersection of two other sets
intersection_update()	&=	    Removes the items in this set that are not present in other, specified set(s)
pop()	 	                    Removes an element from the set
remove()	 	                Removes the specified element
symmetric_difference()	^	    Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()         	|	         Return a set containing the union of sets
update()	        |=	         Update the set with the union of this set and others

'''
#methods on dict:
'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

'''
examples:

dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
c=[9]
c.add(99)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.add(99)
AttributeError: 'list' object has no attribute 'add'
#methods on string
d='highest package'
x='v'
#isupper()
#var.isupper()
x.isupper()
False
#islower()
#var.islower()
x.islower()
True
d.islower()
True
d='RcB'
d.isupper()
False
d.islower()
False
d='RCB3'
d.isupper()
True
x
'v'
+32
32
#upper()
#var.upper()
x.upper()
'V'
d.upper()
'RCB3'
d='highest package'
d.upper()
'HIGHEST PACKAGE'
f='Amelind AAMELE'
f.swapcase()
'aMELIND aamele'
#var.swapcase()
#count()
#var.count('char')
d.count('i')
1
d.count('a')
2
d.count('x')
0
d.count('h')
2
d
'highest package'
#var.count('char',SI)
d.count('h',1)
1
d.count('h',1,3)
0
d.count('h',1,4)
1
d.count_vowels()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d.count_vowels()
AttributeError: 'str' object has no attribute 'count_vowels'
#isdigit()
p='2025rcb'
p.isdigit()
False
p='2025'
p.isdigit()
True
p.index('2')
0
d
'highest package'
d..index('e')
SyntaxError: invalid syntax
d.index('e')
4
d.index('e',5)
14
d.index('z')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    d.index('z')
ValueError: substring not found
d.index('e',5,10)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d.index('e',5,10)
ValueError: substring not found
#find()
d.find('h')
0
d.find('y')
-1
d
'highest package'
d.isalpha()
False
s='vinayaka'
s.isalpha()
True
s='vinayaka STU Kalla'
s.isalpha()
False
s='vinayakaSTUKalla'
s.isalpha()
True
#startswith()
#var.startswith('char\ubstr')
s.startswith('v')
True
s.startswith('vin')
True
s.startswith('aka')
False
#endswith()
x='    naanu  '
#strip()
x.strip()
'naanu'
x.lstrip()
'naanu  '
x.rstrip()
'    naanu'
b='conpused'
b.strip('d')
'conpuse'
f='sakaithussus'
f.strip(s)
'sakaithussus'
f.strip('s')
'akaithussu'
f.strip('su')
'akaith'
f.strip('shi')
'akaithussu'
c='shipratish'
c.strip('h')
'shipratis'
c.strip('sh')
'iprati'
c.strip('ihs')
'prat'
#methods on list
s=[1,20,5,23,3]
s.sort()
s
[1, 3, 5, 20, 23]
s.sort(reverse=True)
s
[23, 20, 5, 3, 1]
d=['rcb','loli','dhanush']
d.sort()
d
['dhanush', 'loli', 'rcb']
s.sort(key=len)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.sort(key=len)
TypeError: object of type 'int' has no len()
d.sort(key=len)
d
['rcb', 'loli', 'dhanush']
d
['rcb', 'loli', 'dhanush']
d.extend(['3',88,99])
d
['rcb', 'loli', 'dhanush', '3', 88, 99]
#tuple
#count,index
#methods set
s={10,20,30}
s.update({22,33,44})
s
{33, 20, 22, 10, 44, 30}
s.update('function')
s
{'u', 10, 'o', 20, 22, 30, 'n', 'i', 33, 'f', 44, 't', 'c'}
x={1,2,3}
s.difference(x)
{33, 'f', 'u', 'o', 10, 44, 't', 20, 'i', 22, 'c', 30, 'n'}
y={3,22,44}
x.difference(y)
{1, 2}
x
{1, 2, 3}
x.difference_update(y)
x
{1, 2}
#intersection()
x.intersection(y)
set()
x={1,2,3}
y={3,22,44}
x.intersection(y)
{3}
x.symmetric_difference(y)
{1, 2, 44, 22}
#discard()
x.discard(3)
x
{1, 2}
x.discard(30)
x.remove(30)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.remove(30)
KeyError: 30
#methods on dict
d={'s':'saaku','b':'beda'}
d.update({'x':10,'v':420})
d
{'s': 'saaku', 'b': 'beda', 'x': 10, 'v': 420}
d.update([[10,20],['s',99]])
d
{'s': 99, 'b': 'beda', 'x': 10, 'v': 420, 10: 20}
d
{'s': 99, 'b': 'beda', 'x': 10, 'v': 420, 10: 20}
#popitem()
d.popitem()
(10, 20)
d
{'s': 99, 'b': 'beda', 'x': 10, 'v': 420}
'''

