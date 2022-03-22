#Student Name and ID: Caleb Seeman A01315336
#Date: Febuary 25th 2022

import getpass
import random

#Creates a global dictionary that refrences all the possible game states you could do this simpilier but I am lazy
win_or_lose = {"rr": "tie", "rp": "lose", "rs": "win", "pp": "tie", "ps": "lose", "pr": "win", "ss": "tie", "sr": "lose", "sp": "win"}

def get_result(choices:str) -> str:
    """
    Simple function used to check the dictionary for the value of the game state:

    examples:

    get_result(rr):

    win_or_lose[rr] = "tie"
    returns "tie"
    """
    return win_or_lose[choices]

def player_game() -> str:
    """
    Function used for a game against another person

    this function will take two inputs through the getpass.getpass function
    after getting each selection it will grab the first character and make it lower case (x[0].lower())

    After this the function checks that both choices are either r p or s (rock paper or scissors)
    
    Next it will add the two strings together to allow for it to be checked in the dictionary
    it will do this in both orders to have better UI later on (This is not need you can do it in one direction and it will be fine)

    After this there is some simple print statements stating who won and who lost, there is also a else statement for when the players tie
    Finally it will return the game state of player 1 (win, lose, tie) so it can be counted in playagain()

    Below this you can see that if either of the players mess up it will tell them and then rerun the function (This is known as recursion)
    """

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
    """
    Starts by taking the users input 

    Then takes the first character and makes it lowercase (player[0].lower())
    next it will create a list of the possible options (r, p, s) and checks that the player has chosen one of those
    
    After this it runs the random.randint function and selects a random number between 0 and 2
    It then uses this as an index to get whether the computer has 'chosen' rock paper scissors

    Finally it will print the result of what happened
    """
    player = getpass.getpass("Rock, Paper, or Scissors? ")
    player = player[0].lower()
    options = ['r', 'p', 's']
    if player in options:
        computer = random.randint(0,2)
        computer = options[computer]
        print(f"You {get_result(player + computer)}")
    else:
        print("That isn't an option please try again")
        computer_game()

def playagain():
    """
    Simple function that will just rerun the main function if the player wants to play again

    also checks to make sure the player said yes or no and if not will rerun playagain function

    Example:

    Would you like to play again?

    Lobster

    Please input 'Yes' or 'No'

    Would you like to play again?

    no
    """
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
    """
    Function that will figure out if you are playing against a computer or a player

    also checks to make sure that you have chosen either player or computer

    Example:

    Would you like to play against the computer or against another player?

    Play against kevin

    Please type either 'another player', or 'the computer'!

    Would you like to play against the computer or against another player?

    another player
    """
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
    """
    Sets up a tournament style game against either a computer or another player
    """
    game_type = input("Would you like to play against the computer or against another player? ")
    game_type = game_type.strip().lower()
    tournament(game_type)

def tournament(opponent:str):
    """
    Firstly checks to ensure that the player has chosen either computer or player (This should be done in the tournament_opponent function but I'm dumb)
    If this condition is not met it will rerun tournament_opponent
    
    Next it will get how many rounds you need to win

    after this it will set the score to 0 for both sides (p1 = 0, p2 = 0)
    Next is a loop that will keep running until either p1 or p2 is equal to the rounds need to win

    This loop runs the player_game or computer_game function respectively

    When either player wins it will print who one and terminate the program
    """
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
    """
    Ignore this it should never be run this is just a file to hold other functions
    """
    infinite()


if __name__ == "__main__":
    main()
