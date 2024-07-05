a=int(input("enter the number "))

# for i in range(1,a+1,1):
#     for j in range(1,i+1,1):
#         print("*",end="")
#     print("\n")
    
for i in range (1,a+1,1):
    # for j in range(a-i+1):
        print(" "*(a-i),end=" ")
    # for j in range(2*i-1):
        print("*"*(i*2-1),end=" ")
    # for j in range(a-i+1):
        print(" "*(a-i),end=" ")
        print("\n")
 

for i in range(1,a+1):
    print("*"*i)
print("\n")
for i in range(1,a+1):
    if(i==1 or i==a):
         print("*"*a)
    else:
         print("*" ,end=" ")
         print(" "*(a-(a-1)) ,end=" ")
         print("*" ,end=" ")
         print(" ")