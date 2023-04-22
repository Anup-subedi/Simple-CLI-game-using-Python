import random

def computer_choice():
    
    choices = {1:'rock', 2:'paper', 3:'scissor'}
    num = random.randint(1,3)
    
    return choices[num]
   

def player_choice():
    
    choice = input("Rock, Paper Or Scissor: ")
    return choice



def win_lose_draw():
    #computer winning conditions
    if player == "exit":
        result = 'exit'
        return result
       
    elif computer =="rock" and player == "scissor" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n---------You lose!-------------\n" 
        return result

    elif computer =="paper" and player == "rock" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n---------You lose!-------------\n" 
        return result

    elif computer =="scissor" and player == "paper" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n---------You lose!-------------\n" 
        return result  
    
    #player wining conditions

    elif computer =="rock" and player == "paper" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n--------You won!--------\n"
        return result

    elif computer =="paper" and player == "scissor" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n--------You won!--------\n"
        return result

    elif computer =="scissor" and player == "rock" :
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n------You won!!--------\n" 
        return result
    #draw condition
    elif computer == player:
        print(f'Computer -> {computer}   You -> {player}' ) 
        result ="\n-------Draw------------\n" 
        return result

    else:
        result = "Invalid input, please try again!"
        return result
print('\n------------------------------------------\n')    
print("-----------ROCK, PAPER OR SCISSIOR---------")
print('\n------------------------------------------\n')   

print('''Game rules: 1.Choose only one object at a time.
2.Wait for another chance till result it out.
3.Enjoy and have fun.
4.Press \'exit\' to exit.\n\n''') 

while True:
    computer = computer_choice()

    player = player_choice()
    player = player.lower()
    if player == 'exit':
        break

    result = win_lose_draw()
    print(result)

