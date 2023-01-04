"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """
    •  TODO: (in progress) Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
            For example, non-number guesses should be handled with an exception.
    •  As a player of the game, I should see a some kind of text header, welcome or game intro message.
    •  A random number should be chosen that is within the range.
    •  As a player of the game, I should be continuously prompted for a guess until I get it right.
    •  TODO: (in progress) As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
    •  As a player of the game, after the game ends I should be shown my number of attempts at guessing.
    •  When the game ends, an ending message is shown to the player.
    EXTRA CREDIT:
    •  As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
            For example, if the range is 1-10 and the player enters 12 they should be informed that this number is outside the range.
    •  As a player of the game, after I guess correctly I should be prompted if I would like to play again.
    •  As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
    •  Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.


    """
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print(f"\n***         NUMBER GUESSING GAME         ***")
    print(f"*** The Number Guessing is easy and fun. Do you think that you can beat the high score? ***\n")

    random_number = random.randrange(1, 10)
    game_over = False
    number_of_attempts = 0
    high_score = 0

    # high score is the lowest of attempts
    # high_score = number_of_attempts

    while game_over == False:
        try:
            #print(f"Random Number (test): {random_number}")  # remove later
            print(f"\nCurrent high score: {high_score}\n")
            player_guess = int(input("INITIAL Guess a number between 1 and 10: "))

            if player_guess < 1 or player_guess > 10:
                print(f"\nOops, try again! Enter a number between 1 and 10\n")
                #number_of_attempts = number_of_attempts - 1 # ask if an attempt outside of the range should be counted as an attempt
                number_of_attempts = 0
            elif player_guess == random_number:
                number_of_attempts += 1
                print(f"You win! Number of attempts: {number_of_attempts}")
                play_again = input("Would you like to play again? (y/n)   ")
                if play_again.lower() == "y":
                    game_over = False
                    random_number = random.randrange(1, 10)
                    if high_score == 0 or high_score == 1:
                        high_score = number_of_attempts
                    elif number_of_attempts < high_score:
                        high_score = number_of_attempts
                    elif number_of_attempts > high_score:
                        high_score
                    number_of_attempts = 0
                elif play_again.lower() == "n":
                    game_over = True
                    random_number = random.randrange(1, 10)
                    number_of_attempts = 0
                    print(f"GAME OVER! Thank you for playing. Have a good day!")
            elif player_guess < random_number:
                print(f"Wrong guess! It's higher.")
                number_of_attempts += 1
            elif player_guess > random_number:
                print(f"Wrong guess! It's lower.")
                number_of_attempts += 1
        except ValueError:
            print("\nOops. Please enter a number only\n")

# Kick off the program by calling the start_game function.
start_game()
