try:
    a= int (input("enter your num : \n"))
    print(a+3)
except Exception as e:
    print("some error has occured",e)