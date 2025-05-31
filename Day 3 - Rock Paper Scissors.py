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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

draw = r'''
.__  __ /\                     .___                              ___ 
|__|/  |)/ ______ _____      __| _/___________ __  _  __  /\    /  / 
|  \   __\/  ___/ \__  \    / __ |\_  __ \__  \\ \/ \/ /  \/   /  /  
|  ||  |  \___ \   / __ \_ / /_/ | |  | \// __ \\     /   /\  (  (   
|__||__| /____  > (____  / \____ | |__|  (____  /\/\_/    \/   \  \  
              \/       \/       \/            \/                \__\ 
'''

win_computer = r'''
                      .__                             ___    
 ___.__. ____  __ __  |  |   ____  ______ ____    /\  \  \   
<   |  |/  _ \|  |  \ |  |  /  _ \/  ___// __ \   \/   \  \  
 \___  (  <_> )  |  / |  |_(  <_> )___ \\  ___/   /\    )  ) 
 / ____|\____/|____/  |____/\____/____  >\___  >  )/   /  /  
 \/                                   \/     \/       /__/   '''

win_player = r'''
                                              .__                   __  .__                 
 __ __  __  _  __ ___________   ____     ____ |  |__   ____ _____ _/  |_|__| ____    ____   
|  |  \ \ \/ \/ // __ \_  __ \_/ __ \  _/ ___\|  |  \_/ __ \\__  \\   __\  |/    \  / ___\  
|  |  /  \     /\  ___/|  | \/\  ___/  \  \___|   Y  \  ___/ / __ \|  | |  |   |  \/ /_/  > 
|____/    \/\_/  \___  >__|    \___  >  \___  >___|  /\___  >____  /__| |__|___|  /\___  /  
                     \/            \/       \/     \/     \/     \/             \//_____/   
  _____                                                    ___                              
_/ ____\___________    ________ _________   ____    /\    /  /                              
\   __\/  _ \_  __ \  /  ___/  |  \_  __ \_/ __ \   \/   /  /                               
 |  | (  <_> )  | \/  \___ \|  |  /|  | \/\  ___/   /\  (  (                                
 |__|  \____/|__|    /____  >____/ |__|    \___  >  \/   \  \                               
                          \/                   \/         \__\                              
'''

possible_choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

#mapping what beats what
winning_cases = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

#player chooses hand
while True:
    player_choice = input("Rock, Paper, Scissors?").strip().lower()
    if player_choice not in possible_choices:
        print("Invalid choice")
        continue
    else:
        break

#computer chooses hand
computer_choice = random.choice(list(possible_choices.keys()))

# showing computer hand
print(f"\nYou chose {player_choice.capitalize()}:\n{possible_choices[player_choice]}")
# win/loss determination
print(f"Computer chose {computer_choice.capitalize()}:\n{possible_choices[computer_choice]}")

#win/loss determination
if computer_choice == player_choice:
    print(draw)
elif winning_cases[computer_choice] == player_choice:
    print(win_computer)
else:
    print(win_player)