import random

word_list = ["aardvark", "baboon", "camel"]
clue=random.choice(word_list)
answer=input('Guess a letter: ').lower()

for x in clue:
  print(x==answer)