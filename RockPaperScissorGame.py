# Rock Paper Scissor Game between you and the computer

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor]

while(True):
    play_game = int(input("\nPress 1 to play the game!\nPress 2 to exit the game!\nEnter your choice: "))
    if play_game == 1:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
        if user_choice >=3 or user_choice < 0:
            print("INVALID INPUT!")
        else:
            print("You chose\n")
            print(game_images[user_choice])
        
            computer_choice = random.randint(0, 2)
            print("Computer chose\n")
            print(game_images[computer_choice])
        
            if user_choice == 0 and computer_choice == 2:
                print("You win!")
            elif user_choice == 1 and computer_choice == 0:
                print("You win!")
            elif user_choice == 2 and computer_choice == 1:
                print("You win!")
            elif user_choice == computer_choice:
                print("It's a Draw!")
            else:
                print("You lose!")        
    else:
        print("Exiting...\nThank You!!")
        break
