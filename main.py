import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list
clue=random.choice(word_list)
guessed=['_'for x in clue]
theend=False
win=False
lose=False
mistakes=0
maxmistakes=len(stages)
tested_letters=[]

print(hangman_art.logo, '\nWelcome to the Hangman The Game.\nHave fun!')
print(guessed)
while not (win or lose):
  answer=input('Guess a letter: ').lower()
  changes=0
  tested_letters+=answer

  for number, letter in enumerate(clue):
    if letter==answer:
      guessed[number]=answer
      changes+=1
  if changes==0:
    mistakes+=1

  if mistakes>0:
    print(stages[-mistakes])
    
  print(guessed,f'\nUsed letters:{tested_letters}')

  if not '_' in guessed:
    win=True
  if mistakes==maxmistakes:
    lose=True
if win==True:
  print('Congratulations, you won a game!')
else:
  print('Maybe next time you will win.')
print(f'The answer was: {clue}')