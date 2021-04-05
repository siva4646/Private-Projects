import random

# Write your code here
languages = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
print("The game will be available soon.")
word = random.choice(languages)
length_word = len(word) - 3
print("Guess the word {}{}".format(word[:3], length_word * '-') + ": ")
guess = input()
if guess == word:
    print("You survived!")
else:
    print("You lost!")