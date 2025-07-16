'''
when class is created it internally divides the memory like key value pairs .
all the properties will be stored in that memory layer.
each property will have a reference address.
the key layer will have an address which will be stored with respect to class name .
when an object is created for a class all the properties of class will be derived to object.
the key layer of object dictionary will have an address which will be stored with respect to object name.
syntax:
access:cname/objectname.pname
modify:cname/objectname.pname=value

key space          | value space
hero
x099

class hero:
    a=10
ob=hero()
ob.a=30
hero.a=20

note:
if a property is modified with respect to classname , will effect all the objects.
if it is modified with respect to an object it effects only for that particular object.

class properties:these are the properties or members which are common for each and every object.
object members are the specific members which are different for every object
example:if a python class is considered as class , students are objects
classname- a1
object-students
cmem-chairs,nannu , board
ob.mem- name , dob , area, phone 

 

'''