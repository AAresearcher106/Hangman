from wordslist import words_list
import random

print("lets play hangman")
play_again = True

while play_again:
        word = list(random.choice(words_list))
        solved = ["_"]*len(word)
        guesses_left = len(word)
        guessed_letters = [] 
        
        while solved != word and guesses_left > 0:
                print(" ".join(solved))
                print(f"{guesses_left} errors left \n")
        
                guess = input("Guess a Letter \n")
        
                if guess in guessed_letters or len(guess) > 1 or not guess.isalpha():
                        print("Invalid input. Please enter a single letter you haven't guessed yet.")
                        continue
        
                guessed_letters.append(guess)
        
                if guess in word:
                        for (i, letter) in enumerate(word):
                                if letter == guess:
                                        solved[i] = letter
        
                else:
                        guesses_left -= 1
                        print("Letter not found in word")
        
        print(''.join(solved))
        
        if(solved == word):     
                print("")
                print("YOU WIN!")
                print("")
                choice = input("Game Over! Would you like to play again? (y/n) \n")

                print("")

                if choice == "n":
                        play_again = False
                        print("Thank you for playing")
                else:
                        play_again = True
        else:
                print(f"You did not get the word and now jimmy gets hurt the word was {''.join(word)}")
                print("""
                          +---+
                          |   |
                          O   |
                         /|\  |
                         / \  |
                              |
                        =========""")

                print("")
                        
                choice = input("Game Over! Would you like to play again? (y/n) \n")

                print("")

                if choice == "n":
                        play_again = False
                        print("Thank you for playing")
                else:
                        play_again = True
