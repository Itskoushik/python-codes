#wap to check if a number is strong number
'''
i=int(input("enter the number: "))
su=0
for j in str(i):
    prd=1
    for z in range(1,int(j)+1):
        prd*=z
    su+=prd
if su==i:
    print("strong number")
else:
    print("not a strong number")
'''
# s=int(input("enter the number: "))
# sum=0
# for i in str(s):
#     prod=1
#     for j in range(1,int(i)+1):
#         prod*=j
#     sum+=prod
# if sum==s:
#     print("strong number")
# else:
#     print("not strong number")
    




#print the pattern (sq matrix pattern)
'''
*****
*****
*****
*****
*****
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):   
#     for j in range(1,n+1):
#         print("*",end="") #same line character
#     print() # new line character 

#q print the pattern (diagonal of sq matrix where i==j)
'''
*
        *
                *
                        *
                                *
                                '''   
        
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("*",end="") #same line character
#         else:
#             print(end="\t") #tab space
#     print() # new line character 



# print this pattern (upper traingle of sq matrix where i<=j)

'''
*****
 ****
  ***
   **
    *
    '''
    
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<=j:
#             print("*",end='') 
#         else:
#             print(" ",end="") #space 
#     print() # new line character 


#print this pattern (lower traingle of sq matrix where i>=j)

'''
*    
**
***
****
*****
'''

# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print("*",end='') 
#         else:
#             print(" ",end="") #space 
#     print() # new line character 

#print this pattern (diagonal=='#')

'''
#****
*#***
**#**
***#*
****#
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print("#",end='')
#         else:
#             print("*",end="") #space 
#     print() # new line character

#print this pattern ()

'''
*****
*   *
*   *
*   *
*****
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         # if i==1 or i==5 or j==1 or j==5:
#         if i in [1,5] or j in [1,5]:
#             print("*",end='')
#         else:
#             print(" ",end="") #space 
#     print() # new line character
    
    
#print this pattern ()

'''
 *** 
*   *
*   *
*   *
 ***
'''
# n=int(input("enter the number for sq matrix pattern: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             if i==j or i==1 and j==n or i==n and j==1:
#                 print(" ",end="")
#             else:   
#                 print("*",end='')
#         else:
#             print(" ",end=" ") #space 
#     print() # new line character


    
#print this pattern ()

'''
****  
*   *
****
*   *
****
'''
n=int(input("enter the number for sq matrix pattern: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==5 or i in range(1,n+1,2):
            if j==5 and i in range(1,n+1,2):
                print(" ",end=" ")
            else:  
                print("*",end='')
        else:
            print(" ",end="") #space 
    print() # new line character
    

    
