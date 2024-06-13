while(True):
    age = int (input("enter your age in number : \n"))

    if(age<13):
        print("Children")
    elif(age>=13 and age<=19):
        print("Teenagers")
    elif(age>=20 and age<=59):
        print("Adult")
    else:
       print("Senior")