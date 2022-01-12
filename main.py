import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
clue=random.choice(word_list)
guessed=['_'for x in clue]
theend=False
win=False
lose=False
mistakes=0
maxmistakes=len(stages)
print(guessed)

print('Welcom to the Hangman the game.\nHave fun!')

while not (win or lose):
  answer=input('Guess a letter: ').lower()
  changes=0
  for number, letter in enumerate(clue):
    if letter==answer:
      guessed[number]=answer
      changes+=1
  if changes==0:
    mistakes+=1

  if mistakes>0:
    print(stages[-mistakes])
    
  print(guessed)

  if not '_' in guessed:
    win=True
  if mistakes==maxmistakes:
    lose=True
if win==True:
  print('Congratulations, you won a game!')
  else:
    print('Maybe next time.')