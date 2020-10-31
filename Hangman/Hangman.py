'''
Hangman.py
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)
        iter_char = dict.fromkeys(word,0)
        guesses = 0
        increase = lambda x:x+1
        while guesses < 10:
            ch = input('Enter a guess:').lower()
            self.printword()

            ### Your code goes here:###
            if len(ch) != 1:
                print("Only one character is allowed in each input.")
            if len(ch) == 0 or ch.isalpha()==False:
                print("Only allow alphabetic characters.")
            if ch not in iter_char.keys():
                print("Does not occur")
                guesses = increase(guesses)
                print("You have " + str(10-guesses) + " chances left.")
            if ch in iter_char.keys():
                iter_char[ch] = increase(iter_char[ch])
                if iter_char[ch] <= 1:
                    self.wordguess[list(iter_char.keys()).index(ch)] = ch
                else:
                    print("You already guessed this character.")
            if all(value >= 1 for value in iter_char.values()) == True:
                print("Congratulations!")
                exit()
        print('Sorry dude, the word is ' + word)

if __name__ == "__main__":

    game = Hangman()

    game.playgame()