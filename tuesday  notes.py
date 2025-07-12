#print this pattern ()

'''
*      *
  *  *
    *
  *  *
*      *
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i+j==n+1:
#             print("*",end="")
            
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character

#print this pattern ()

'''
*****
*
*****
*
*****
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i in range(1,n+1,2) or j==1:
#             print("*",end="")
            
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character


#print this pattern ()

'''
    *     
  *   *
*       *
* * * * *
*       *
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i ==4 or j in (1,n) and i in range(3,n+1) or i==2 and j in (n-3,n-1) or i==1 and j==3:
#             print("*",end=" ")
            
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character

#print this pattern ()

'''
1
2 4
1 2 3
2 4 6 8
1 2 3 4 5
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             if i%2==0:
#                 print(j*2,end=" ")
#             else:
#                 print(j,end=" ") 
            
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character
    
#print this pattern ()
'''
a
a b
a b c
a b c d
a b c d e
'''
# n=int(input("enter the number for sq matrix pattern: "))
# a=input("enter the alphabet ")
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(chr(64+j),end=" ") # or we can use chr(ord(a)-1+j)
            
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character

# s=input("enter the string: ")

# s="nyaya andre nyana gandumaklu nyaya"
# s=s.split()
# l=[]
# for i in s:
#     rev=""
#     for j in i:
#         rev=j+rev
#     l+=[rev]
# print(" ".join(l)) 
 
       
# s="nyaya andre nyana gandumaklu nyaya".split()
# sen=""
# for i in s:
#     word=""
#     for j in i:
#         word=j+word
#     sen+=word+" "
# print(sen)    

# s=input("enter the string: ").split()
# sen=""
# for i in s:
#     word=""
#     for j in i:
#         word=j+word
#     sen+=word+" "
# print(sen)





# join() function works  on collections like homo collections like str,list,tuple,dict
# it is a function which is used to concatenate strings based on a specific delimiter or character 
# for string it adds the gluestring after all characters .

'''
#syntax
gluestring.join(var)

#examples
x="habibi come to dubai".split()
print(' '.join(x)) 
print("***".join(x))

#remove print when using a terminal or idle interpreter

output
habibi come to dubai
habibi***come***to***dubai


x="habibiiiiii"
print(' '.join(x)) 
print("***".join(x))

output
h a b i b i i i i i i
h***a***b***i***b***i***i***i***i***i***i

'''

#question
#print bangalu bangari feeling adhuri as adhuri feeling bangari bangalu 
# print(" ".join(input("enter the string: ").split()[::-1]))


