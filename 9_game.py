from ast import Break
import random
while(True):
    print("\nLets start the game....")
    print("enter your choice\nr: Rock\np: Paper\ns: Scissor")
    your_choice=input("-->")
    your_choice=your_choice.lower()
    choices={'r':'Rock','p':'Paper','s':'Scissor'}
    print("You choose-->",choices[your_choice])
    choi=['r','p','s']
    computer_choice=random.choice(choi)
    print("Computer choose-->",choices[computer_choice])
    if(computer_choice==your_choice):
        print("Match tie...!")
    elif (your_choice=='r' and computer_choice=='s' or your_choice=='p' and computer_choice=='r' or your_choice=='s' and computer_choice=='p'):
        print("You win...!")
    else:
        print("Computer win...!")
    
