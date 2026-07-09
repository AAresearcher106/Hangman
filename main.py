from wordslist import words_list
import random

print("Let's play hangman!")
word = list(random.choice(words_list))
solved = ["_"]*len(word)
guesses_left = 5
guessed_letters = [] 

while solved != word and guesses_left > 0:
	print(" ".join(solved))
	print(f"{guesses_left} guesses left \n")

	guess = input("Guess a Letter \n")

	if guess in guessed_letters or len(guess) > 1:
		continue

	guessed_letters.append(guess)

	if guess in word:
		for (i, letter) in enumerate(word):
			if letter == guess:
				solved[i] = letter

	else:
		guesses_left -= 1

print(''.join(solved))

if(solved == word):
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
