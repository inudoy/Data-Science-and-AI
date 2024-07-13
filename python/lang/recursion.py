# def factorial(n):
#     if(n==1 or n==0):
#         return n
#     else:
#         return n*factorial(n-1)

# def sum_natural(n):
#     if(n==0):
#         return 0
#     else:
#         return n + sum_natural(n-1)
    

# def pattern(n):
#     if(n==0):
#         print(" ")
#     else:
#         print("*"*n)
#         pattern(n-1)
        
    
# n=int(input("enter your input in numeric : \n"))
# print(factorial(n))
# print(sum_natural(n))
# print(pattern(n))

def function(l , word):
    li=[]
    for i in l:
        if not(i==word):
            li.append(i.strip(word))
    return li
l=["hallo","ballo","jali","llo"]
print(function(l,"llo"))