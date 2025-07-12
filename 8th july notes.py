#wap to check whether the two strings are anagrams or not
# def are_ana(s1, s2):
    
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2) 

# print(are_ana("mother in law","hilter woman"))


#wap to check entered string is panagram or not
# def is_panagram(s):
#     a = set("abcdefghijklmnopqrstuvwxyz")
#     s = s.replace(" ","").lower() 
#     st=""
#     for i in s:
#         if i in a and i.isalpha():
#             st+=i
#     return len(st) == 26
#     #return set(s)>=a
        
# is_panagram("The quick brown fox jumps over the lazy dog")

#wap to check whether the entered string is isogram or not
# def is_isogram(s):
#     s = s.replace(" ", "").lower()
#     low="abcdefghijklmnopqrstuvwxyz"
#     for i in s:
#         if s.count(i) > 1 or i not in low:
#             return False
#     else:
#         return True
        
# print(is_isogram("karan"))






#wap to print nth fibonacci series 
n=int(input("Enter the number of terms in Fibonacci series: "))
a, b = 0, 1
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

for i in range(n): print(a, end=' '); a, b = b, a + b

