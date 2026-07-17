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
        helped_used = False

        #Main gameplay loop of prompting user
        while solved != word and guesses_left > 0:
                #Prints user progress
                print(" ".join(solved))
                print(f"{guesses_left} errors left \n")

                #Prompts user
                guess = input("Guess a Letter, the whole word, or type 'help' for a hint \n").lower()
                print("")

                if guess == "help":
                        if help_used:
                                print("")
                                print("You have already used a hint this round")
                                print("")
                        else:
                                help_used = True
                                if guessed_letter:
                                        print(f"Letters already guessed: {', '.join(sorted(guessed_letter))}")
                                else:
                                        print("No letters guessed yet.")
                                remaining = [l for l in word if l not in guessed_letters and l not in solved]
                                if remaining:
                                        hint = random.choice(remaining)
                                        guessed_letters.append(hint)
                                        for (i, letter) in enumerate(word):
                                                if letter == hint:
                                                        solved[i] = letter
                                        print(f"Free letter revealed: {hint.upper()}")
                                else:
                                        print("No hidden letters left to reveal")
                        continue

                #Checks that guess is valid
                 if len(guess) >= 5:
                        if list(guess) == word:
                                solved = word
                        else:
                                print(f"Wrong! The word was not '{guess}'. You lose!")
                                guesses_left = 0
                        continue

                if guess in guessed_letters or not guess.isalpha() or 1 < len(guess) < 5:
                        print("Invalid input. Please enter a single letter, or a full word.")
                        continue
        
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
        print(''.join(solved))
        if(solved == word): 
                print("")
                print("YOU WIN!")
                print("")

                #choice = input("Game Over! Would you like to play again? (y/n) \n")
                #print("")
                #if choice == "n":
                        #play_again = False
                        #print("Thank you for playing")
                #else:
                        #play_again = True

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
                
