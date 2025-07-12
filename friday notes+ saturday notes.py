#wap to get following output 
# s="rajankunte rakesha jallahalli joela"
# output---> "retnuknaja rahseka jillahalla jaleo"
# def dell(s):
#     stw=[]
#     for i in range(len(s)):
#         stw.append(s[i][0] + s[i][:0:-1])
#     print(" ".join(stw))        
# s=input("enter the string: ").split()
# dell(s)

#wap to get the output
#number---> even then number divide by 2 
#number---->odd then number multiply by 3 + 1
#do this until we reach 1 and then count the number of times we have done an operation 

#example
#enter  the number: 5
#5 is the number of the times the loop has run
'''
16
8
4
2
1
'''


# def jujubi(i):
#     j=0
#     while i!=1:
#         if i%2==0:
#            i=i//2
#            print(i)
#         else:
#             i=i*3+1
#             print(i)
#         j+=1       
#     print(j,"is the number of the times the loop has run") 
# jujubi(int(input("enter  the number: ")))      

#3. function without any argument with return type
'''
it is type of function which doesnt contain any arguments but will have return in it.

return keyword is used to terminate the function . once its executed it doesnt go to next lines of program written
under it .
it can be used in function with or without having values

syntax:
def some():
    a=int(input("enter")) 
    b=int(input("enter"))
    return a+b,a-b,a/b,a
print(some())

a,s,d,n=some()
print(a)
print(s)

res=some()
print(res)
  

'''
#wap to get following output
# ['.in', '.py', '.xlx', '.txt']

# input: 
# x=["amazon.in","python.py","excel.xlx","doc.txt"]
# def prog():
#     x=["amazon.in","python.py","excel.xlx","doc.txt"]
#     l=[]
#     for i in x:
#         j=i.split(".")
#         l+=["."+j[1]]
#     print(l)
    
# prog()

#wap to get following output
# {'com': ['amazon', 'google'], 'in': ['myntra'], 'py': ['prog']}
# input:x=["amazon.com","google.com","myntra.in","prog.py"]

# def ggs():
#     x=["amazon.com","google.com","myntra.in","prog.py"]
#     dic={}
#     for i in x:
#         w,dom=i.split(".")
#         print(w,dom)
#         if dom not in dic:
#             dic[dom]=[]
#         dic[dom].append(w)
        
#     return dic    
# print(ggs())

#4.function with argument and return values:
'''
it is type of function which requires argument and also return 
syntax:
def fname(arg1,arg2......argn):
    sb
    return val1,val...valn
print(fname(val1,val2....valn))

'''
#wap to find of 3 int numbers:
# def prod(a,b,c):
#     return a*b*c
# print(prod(int(input("enter the number1: ")),int(input("enter the number2: ")),int(input("enter the number3: "))))
#wap to count the no of uppercase characters in string collections.

# def cu():
#     s=input("enter the string: ")
#     c=0
#     for i in s:
#         if i.isupper():
#             c+=1
#     print(c)
# cu()

# def cut():
#     s=input("enter the string: ")
#     c=0
#     for i in s:
#         if i.isupper():
#             c+=1
#     return c
# print(cut())             
        
# def cute(s):
#     c=0
#     for i in s:
#         if i.isupper():
#             c+=1
#     return c
# print(cute(input("enter the string: ")))   

# def cutee(s):
#     c=0
#     for i in s:
#         if i.isupper():
#             c+=1
#     print(c)
# cutee(input("enter the string: "))  


# def add(a,b):
#     return sum(a,b)
# def sub(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def divi(a,b):
#     return a/b
# def get_val():
#     a=int(input("enter number 1: "))
#     b=int(input("enter number 1: "))
#     return a,b
    
# print("------enter 1 to do addition operation")
# print("------enter 2 to do substraction operation")
# print("------enter 3 to do multiplication operation")
# print("------enter 4 to do division operation")
# print("------enter 5 to do exit.")
# while True:
#     c=int(input("enter the operation code: "))
#     if c==1:
#         a,b=get_val()
#         print(f"sum of {a} and {b} numbers is: {add(a,b)}")
#     elif c==2:    
#         print(f"subs of {a} and {b} numbers is: {sub(a,b)}")
#     elif c==3:   
#         print(f"multi of {a} and {b} numbers is: {multi(a,b)}")
#     elif c==4:        
#         print(f"division of {a} and {b} numbers is: {divi(a,b)}")
#     elif c==5:        
#         print("Exiting...........")
#     else:
#         print("pls enter correct code..")
    
        
#wap to return first maximum of a homo list of int

# l=eval(input("enter the list:"))
# max=l[0]
# for i in range(1,len(l)):
#     if max<l[i]:
#         max=l[i]
# print(max)

# max function and min function       
    
 