chai_type = {
    "masala": "spicy",
    "ginger": "zesty",
    "green": "mild"
}

for i in chai_type:
   
    print(f"Chai type: {i}, Description: {chai_type[i]}")
    print("----------------------------------------------")
      
    print(i,"--",chai_type[i])
print("----------------------------------------------end\n")
for key , values in chai_type.items():#it will get all the items with key also
    print("3rd method-------------\n")
    print(key,values,"\n")
        

#another thing 
square={
    x:x**2 for x in range(4,10,2)
}
for i in square:
    print(i,"---",square[i])
    

