'''
global and local scope:
global scope: these are variables which are declared outside of function ,
it can be accessed inside and outside the function . 
a keyword global is used to makes a local variable  accessed noutside the function.
local scope: these are variables which are declared inside the function 
it can be accessed only inside method area or local space

d=22
def new():
    d=10
    p=23
    print(d)
    print(p)
print("all the best")
new()
print(d)
print(p)


output:
all the best
10
23
22
Traceback (most recent call last):
  File "c:\Users\koushik\Downloads\python codes\9th july notes.py", line 29, in <module>
    print(p)
          ^
NameError: name 'p' is not defined

_____global__space___|____local__space___
d=22                 | d=10
new [0x88]           | p=23
print(d)             | print(d)
print(p)             | print(p)


using global keyword
d=22
def new():
global d,p
    d=10
    p=23
    print(d)
    print(p)
print("all the best")
new()
print(d)
print(p)


_____global__space___|____local__space___
                     |global d,p
d=22                 | d=10 
new [0x88]           | p=23
print(d)             | print(d)
print(p)             | print(p)




x=24
def chandru():
    p=100
    print(x)
    def shekar():
        q=8
        print(q)
        print(p,p)
        print(x)
    print(p)
    shekar()
    print(p+p)
print("paahimaa")
chandru()
print(x)

paahimaaa
24
100
8
100 100
24
200
24

local variables can be accessed only in method area that is ,it can be accessed inside the function and its nested functions 
when a local vaiable is modified inside nested function , it effects only in that particular function 
if a local variable have to be modified inside nested function which in tern have to affected outside that particular function
non local keyword will be used 


non local searches for a local variable outiside that function , if not present or 
we have declared global then it doesnt work as locally there are no local variables available so that
non local works.
'''
#wap to print nth fibonacci series 
n=int(input("Enter the number of terms in Fibonacci series: "))
a, b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

for i in range(n): print(a, end=' '); a, b = b, a + b
