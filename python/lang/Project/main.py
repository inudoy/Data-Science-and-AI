import random 

menu = '''
      If you want to play, click 1
      If you want to Quit, click 2
      '''
print(menu)

b = input("Enter 1 or 2: \n")

while b != "2":
    if b == "1":
        computer = random.choice([1, -1, 0])
        human = {"r": 1, "p": -1, "s": 0}
        show = {1: "r", -1: "p", 0: "s"}
        
        a = input("Enter r (rock), p (paper), or s (scissors) as choices: \n")
        if a in human:
            human_value = human[a]

            print(f"You have chosen {show[human_value]} and opponent has chosen {show[computer]}.\n")

            if human_value == computer:
                print("Draw!\n")
            elif (human_value == 1 and computer == -1) or (human_value == -1 and computer == 0)  or  (human_value == 0 and computer == 1):
                 
                
                print("You win!\n")
            else:
                print("Computer wins!\n")
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.\n")
    else:
        print("Invalid input. Please enter 1 to play or 2 to quit.\n")
    
    print(menu)
    b = input("Enter 1 or 2: \n")

print("Game ended.")
