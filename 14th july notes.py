'''
Recursion:
recursion is the phenomenon of calling a function again and again or a function calling itself until termination
condition is True.
the advantage of using recursion is it reduces the instructions but the disadvantage of recursion is
it consumes more memory and time.
it also increases the complexity of the program.
syntax:
1.without return values:
def fname(args):
    if cond:
        return
    fname(values)  # function calling itself
fname(values)

2.with return values:
def fname(args):
    if cond:
        return values
    return fname(values) #recursive call
print(fname(values))  # actual function call

factorial of a number using recursion:
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1) #recursive call
print(fact(3)) # actual function call

steps to convert looping program to recursive program:
1.initialise all the variables including the looping variables in the function declaration 
2.write the termination condition opposite to the looping condition in the form of if statement.
3.return the total result or final result inside the if statement.
4.write the logic of the program as it is excluding the initialisation or updatation.
5.increment or decrement must be done in recursive call.

these points are not applicable for all the programs .





'''
#wap the count the number of uppercase characters in a string using recursion:
# def count(st,c=0,i=0):
#     if i == len(st):
#         return c
#     if st[i].isupper():
#         c += 1
#     return count(st, c, i + 1)  # recursive call
# print(count(input("Enter the string: ")))

#wap to extract all the complex numbers in list collection.
# def ext_com(l,li=[],i=0):
#     if i==len(l):
#         return li
#     if type(l[i]) == complex:
#         li.append(l[i])
        
#     return ext_com(l,li,i+1)
# print(ext_com(eval(input("enter the list: "))))  

#wap to reverse a string
# def rev_str(s,rev="",i=0):
#     if i==len(s):
#         return rev
#     rev=s[i]+rev
#     return rev_str(s,rev,i+1)
# print(rev_str(input("enter the string : ")))

#wap to get the output single digit if 838 is passed keep doing sum 
# def sum_digit(n):
#     if len(str(n))==1:
#         return n
#     s=0
#     for i in str(n):
#         s+=int(i)
#     return sum_digit(s)
# sum_digit(int(input("enter the integer :")))

# l=[333,["saku","vin",2],({1,9,(10,5,"bye",(25,5))})]

# for i in l:
#     if type(i) in (list,tuple):
#         for j in i:
#             if type(j)==int:
#                 sum+=j
#     elif type(i)==set:
        


        
# l=[333,["saku","vin",2],({1,9,(10,5,"bye",(25,5))})]
# print(sum_int(l))
def sum_int(l, sum=0):
    for i in l:
        if type(i) == int:
            sum += i
        elif type(i) in (list, tuple, set):
            sum += sum_int(i)
    return sum
