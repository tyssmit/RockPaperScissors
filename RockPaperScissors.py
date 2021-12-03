import random

while(True):
    pc_choice=random.randint(1,3)
    #assigning numbers to rock, paper, or scissors
    if(pc_choice==1):
        pc_choice="Rock"
    elif(pc_choice==2):
        pc_choice="Paper"
    else:
        pc_choice="Scissors"
#testing pc choice
#print(pc_choice)
    #main menu
    print("Welcome to the Rock Paper Scissors Machine")
    print("Lets start!!!")
    print("To select Rock press 1")
    print("To select Paper press 2")
    print("To select Scissors press 3")
    print("--------------------------")
    print("")
    try:
        user=int(input())
    except ValueError:
        print("please enter a valid number")
        continue
    if(user==1):
        user="Rock"
        print("You chose Rock")
        if(pc_choice=="Rock"):
            print("The PC also chose Rock")
            print("Try Again")
            print("")
        elif(pc_choice=="Paper"):
            print("The PC chose Paper")
            print("Try Again")
            print("")
        else:
            print("The PC chose Scissors")
            print("You Won!!!")
            print("")
            print("to play again press Y if not press anything else")
            again=input()
            if(again=="y" or again=="Y"):
                continue
            else:
                break
    elif(user==2):
        user="Paper"
        print("You chose Paper")
        if(pc_choice=="Paper"):
            print("The PC also chose Paper")
            print("Try Again")
            print("")
        elif(pc_choice=="Scissors"):
            print("The PC chose Scissors")
            print("Try Again")
            print("")
        else:
            print("The PC chose Rock")
            print("You Won!!!")
            print("")
            print("to play again press Y if not press anything else")
            again=input()
            if(again=="y" or again=="Y"):
                continue
            else:
                break
    elif(user==3):
        user=="Scissor"
        print("You chose Scissors")
        if(pc_choice=="Scissors"):
            print("The PC also chose Scissors")
            print("Try Again")
            print("")
        elif(pc_choice=="Rock"):
            print("The PC chose Rock")
            print("Try Again")
            print("")
        else:
            print("The PC chose Paper")
            print("You Won!!!")
            print("")
            print("to play again press Y if not press anything else")
            again=input()
            if(again=="y" or again=="Y"):
                continue
            else:
                break
    else:
        continue