#Importing modules to randomly select words
from wordslist import words_list
import random

#Initiating the game
print("Let's play hangman!")
play_again = True

while play_again:
        #Picks random word, initializes user progress and lives
        #user progress includes both progress on the word and failed guesses
        word = list(random.choice(words_list))
        solved = ["_"]*len(word)
        guesses_left = 6
        guessed_letters = [] 

        #Main gameplay loop of prompting user
        while solved != word and guesses_left > 0:
                #Prints user progress
                print(" ".join(solved))
                print(f"{guesses_left} errors left \n")

                #Prompts user
                guess = input("Guess a Letter \n")

                #Checks that guess is valid
                if guess in guessed_letters or len(guess) > 1 or not guess.isalpha():
                        print("Invalid input. Please enter a single letter you haven't guessed yet.")
                        continue

                #Adds guess to progress
                guessed_letters.append(guess)
        
                if guess in word:
                        for (i, letter) in enumerate(word):
                                if letter == guess:
                                        solved[i] = letter
        
                else:
                #Punishes user for wrong guess
                        guesses_left -= 1
                        print("Letter not found!")
        
        print(''.join(solved))

        #End messages which change if the user wins or loses
        #Ask the player if they want to play again
        #Reprompt if input is not yes or no
        if(solved == word): 
                print("")
                print("YOU WIN!")
                print("")

                choice = 1
                while choice != "no" and choice != "yes":
                        choice = input("Play again? (yes/no) \n").lower()

                        print("")

                        if choice == "no":
                                play_again = False
                                print("Thank you for playing")
                                
                        if choice == "yes":
                                play_again = True

                        else: 
                                print("Invalid input.")
        else:
                print(f"Out of lives, game over! The word was {''.join(word)}")
                print("""
                          +---+
                          |   |
                          O   |
                         /|\  |
                         / \  |
                              |
                        =========""")

                print("")

                choice = 1
                while choice != "no" and choice != "yes":
                        choice = input("Play again? (yes/no) \n").lower()

                        print("")

                        if choice == "no":
                                play_again = False
                                print("Thank you for playing")
                                
                        elif choice == "yes":
                                play_again = True

                        else: 
                                print("Invalid input.")
                
