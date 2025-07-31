#user defined functions
'''
these are the functions which are created based on user requirement.
in python to create a function def keyword is used
syntax:

def functionname(argument1,aug2.....argn): -----> func declaration 
    S.B                           ------> function definition 
    return v1,v2,v3,v4...vn
fname(val1,val2,val3,val4...valn)    ----> function call


based on argument and returning val user defined func are of 4 types:
    function without args and without return
    function without args and return
    function with args and without return
    function with args and with return
    

1. function without args and without return: 
it is type of function which doesnt require any argument or any return 

example:
def fname():
    s.b
fname()

memory diagram:

      global space            local space
_______main space___|________method area________
                    |     0X18
        add         |     a=int(input("enter:"))
        0X18        |     b=int(input("enter:"))
                    |     print(a+b)
                    |
The execution starts from main space where it will have the name of the function with the address 
the instructions will be stored in the method area.
when a function is called, it will execute the instructions based on address . 

'''
#WAP to check if the enter string is palindrome or not 

# def palin():
#     s=input("enter the string: ")
#     i=0
#     rev=""
#     while i<len(s):
#         rev=s[i]+rev
#         i+=1
#     if rev==s:
#         print(s," is palindrome.")
#     else:
#         print(s,"is not palindrome")
# palin()


#wap to find sum of all the even digits present in a string collection:
# def evend():
#     s=input("enter the string: ")
#     sum=0
#     for i in s:
#         if i.isdigit() and int(i)%2==0:
#             sum+=int(i)
                
#     print(sum,"is the sum of all even digits in string.")
# evend()

#consider an integer number with min 3 digits , check whether the sum of the individual digits is a perfect number 
# def perfnum():
    
#     i=int(input("enter the number: "))
#     sum=0
#     while i!=0:
#         ld=i%10
#         sum+=ld
#         i=i//10
#     p=0
#     i=1
#     while i<sum:
#         if sum%i==0:
#             p+=i
#         i+=1
#     if sum==p:
#         print(sum,"it is a perfect number ")
#     else:
#         print(sum,"it is not perfect number")
        
# perfnum()    

#2.functions with arguments and no return  
# it is type of function where the arguments are passed but it doesnt contain return in it 
'''
syntax  (or) example
def add(a,b):
    print(a+b)
add(3,10)

note: the number of arguments must be equal to number of values.

'''    
#wap to extract all the palindrome strings present in tuple collection.

# def extstr(t):
#     ext=[]
#     for i in t:
#         if type(i)==str:
#             if i==i[::-1]:
#                 ext+=[i]
#     print(ext)
# t=eval(input("enter tuple: "))
# extstr(t)
        
# def extstr(t):
#     ext=()
#     for i in t:
#         if type(i)==str:
#             if i==i[::-1]:
#                 ext+=(i,)
#     print(ext)

        

    
    
    
    