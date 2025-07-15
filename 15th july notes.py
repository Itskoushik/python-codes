#wap to count the number of palidrome string present in list collection

# l=eval(input("enter the list: "))
# c=0
# for i in l:
#     if type(i)==str and i==i[::-1]:
#         c+=1
# print(f"the count of palindrome strings in list is {c}")
        
# l=eval(input("enter the list: "))
# i,c=0,0
# while i<len(l):
#     if type(l[i])==str and l[i]==l[i][::-1]:
#         c+=1
#     i+=1
# print(f"the count of palindrome strings in list is {c}")

# l=eval(input("enter the list: "))
# c=0
# for i in range(len(l)):
#     if type(l[i])==str and l[i]==l[i][::-1]:
#         c+=1
# print(f"the count of palindrome strings in list is {c}")  



# def count_pali(s,c=0,i=0):
#     if i==len(s):
#         return c
#     if type(s[i])==str and s[i]==s[i][::-1]:
#         c+=1
#     return count_pali(s,c,i+1)
# print(count_pali(["amma",12,"exe"]))


#print fibonacci series using recursion

def fibonacci(n,i=0,a=0,b=1):
    if i==n-1:
        return a
    print(a,end=" ")
    return fibonacci(n,i+1,b,a+b)
print(fibonacci(int(input("enter the no of values in fibonacci series: "))))
    
# i=int(input("enter how many fibonacci series u want: "))
# a=0
# b=1
# print(a,end=" ")
# for i in range(i-1):
#     a,b=b,a+b
#     print(a,end=" ")