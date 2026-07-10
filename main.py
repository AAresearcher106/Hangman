from wordslist import words_list ###list where Hangman code comes from
import random

print("Let's play hangman!")

###Picks a random word from the list, generates a list representing the user's progress on that word.
word = list(random.choice(words_list))
solved = ["_"]*len(word)

###Defines number of lives and initializes the guessed letters list.
guesses_left = 6
guessed_letters = [] 

while solved != word and guesses_left > 0: ###Below code only executes when word is unsolved and user has guesses left over
	### prints out the user's progress, lives, and prompts an input.
	print(" ".join(solved))
	print(f"{guesses_left} guesses left \n")

	guess = input("Guess a Letter \n")

	if guess in guessed_letters or len(guess) > 1:
		continue ### skipping already-guessed letters and bad inputs
	
	guessed_letters.append(guess) ###Adds guessed letters to stored list

	if guess in word:
		### determines position of each letter corresponding to a correct guess
		for (i, letter) in enumerate(word):
			if letter == guess:
				solved[i] = letter
	

	else:
		guesses_left -= 1
		### removes a life for wrong guesses

print(''.join(solved))
###printing user's progress

if(solved == word): ###Win or lose conditional, ends round
	print("YOU WIN!")
else:
  print(f"You did not get the word and now jimmy gets hurt the word was {''.join(word)}")
  print("""
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
	=========""")
