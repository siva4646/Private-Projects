from random import randint

print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']
secret_word = words[randint(0, 3)]
word = secret_word)

guess = input(f"Guess the word: {word}")

if guess == secret_word:
    print('You survived!')
else:
    print('You lost!')