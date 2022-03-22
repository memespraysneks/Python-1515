#Student Name and ID: Caleb Seeman A01315336
#Date: Febuary 25th 2022

import getpass
import random

win_or_lose = {"rr": "tie", "rp": "lose", "rs": "win", "pp": "tie", "ps": "lose", "pr": "win", "ss": "tie", "sr": "lose", "sp": "win"}

def get_result(choices):
    return win_or_lose[choices]

def player_game():
    player_1 = getpass.getpass("Player 1: Rock, Paper, or Scissors? ")
    player_1 = player_1[0].lower()
    player_2 = getpass.getpass("Player 2: Rock, Paper, or Scissors? ")
    player_2 = player_2[0].lower()
    if player_1 in ['r', 'p', 's']:
        if player_2 in ['r', 'p', 's']:
            p1p2 = player_1 + player_2
            p2p1 = player_2 + player_1

            p1p2end = get_result(p1p2)
            p2p1end = get_result(p2p1)
            if p1p2end != "tie":
                print(f"Player 1 you {p1p2end}, Player 2 you {p2p1end}")
            else:
                print(f"You {p1p2end}!")
            return p1p2end
        else:
            print("Player 2 you messed up your input try again!")
            player_game()
    else:
        print("Player 1 you messed up your input try again!")
        player_game()

def computer_game():
    player = getpass.getpass("Rock, Paper, or Scissors? ")
    player = player[0].lower()
    options = ['r', 'p', 's']
    computer = random.randint(0,2)
    computer = options[computer]
    print(f"You {get_result(player + computer)}")

def playagain():
    user_input = input("Would you like to play again? ")
    user_input.lower().strip()
    if user_input == "yes":
        main()
    elif user_input == "no":
        return
    else:
        print("Please input 'Yes' or 'No'")
        playagain()

def infinite():
    game_type = input("Would you like to play against the computer or against another player? ")
    game_type.strip().lower()
    if game_type == "another player":
        player_game()
    elif game_type == "the computer" or "computer":
        computer_game()
    else:
        print("Please type either 'another player', or 'the computer'!")
        infinite()
    playagain() 

def tournament_opponent():
    game_type = input("Would you like to play against the computer or against another player? ")
    game_type = game_type.strip().lower()
    tournament(game_type)

def tournament(opponent):
    if opponent == "another player":
        rounds = int(input("How many rounds do you need to win, to win the tournament? "))
        p1 = 0
        p2 = 0
        while p1 < rounds and p2 < rounds:
            result = player_game()
            if result == "win":
                p1 += 1
            if result == "lose":
                p2 += 1
        if p1 >= rounds:
            print("Player1 wins the tournament!")
        else:
            print("Player2 wins the tournament!")
    elif opponent == "computer":
        rounds = input("How many rounds do you need to win the tournament? ")
        p1 = 0
        p2 = 0
        while p1 < rounds and p2 < rounds:
            result = computer_game()
            if result == "win":
                p1 += 1
            if result == "lose":
                p2 += 1
        if p1 >= rounds:
            print("Player1 wins the tournament!")
        else:
            print("The computer wins the tournament")
    else:
        print("Please input either 'computer' or 'another player'")
        tournament_opponent()

def main():
    infinite()


if __name__ == "__main__":
    main()
