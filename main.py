import random

word_list = ["aardvark", "baboon", "camel"]
clue=random.choice(word_list)
answer=input('Guess a letter: ').lower()

guessed=['_'for x in clue]
for number, letter in enumerate(clue):
  if letter==answer:
    guessed[number]=answer
print(guessed)