a=int(input("enter the numbeer till 3\n"))

match a:
    case 1:
        print("1 * 1 = ",a*a)
    case 2:
        print("1 * 2 = ",1*a)
    case 3:
        print("1 * 3 = ",1*a)
    case _:
        print("end of the program default",a)