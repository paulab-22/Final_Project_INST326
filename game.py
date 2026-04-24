import random

import pandas as pd


#Player class
#also might need a function to check if the player has letters for a word
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
    def add_letter(self, letter):
        pass

#class for the die
class Die:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        pass
    
class ConsonantDie(Die):
    def __init__(self):
        super().__init__(["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"])

class VowelDie(Die):
    def __init__(self):
        super().__init__(["A", "E", "I", "O", "U"])
        

#Scoring
class ScoringSystem:
    def calculate_score(self, words):
        """calculates score for the turn
        Algorithm skeleton
        """
        total_score = 0
    
        #1 loop through word
        #2 calculate score total based on letter values
        #3 length multiplier
        #4 add calculated turn score to toal
    

class Game:
    def __init(self):
        self.players = []
        
    def setup_players(self):
        pass
    def play_turn(self):
            while round <= 10:
                round += 1
            else:
                pass
    def play(self):
        pass

class WordManager:
    def __init__(self):
        self.bank = pd.read_csv('word_bank.csv')
        self.bank = self.bank[self.bank['word'].str.len() >= 3]

    def isInWordBank(self, word):
        words = self.bank[self.bank['word'].str.upper() == word.upper()]
        return len(words) > 0
    
def main():
    game = Game()
    game.play()
    
if __name__ == "__main__":
    main()
    
# Starting the game and the game setup

print("WELCOME TO MY WORDSMITH GAME")
total_rounds = 10

score_1 = 0
score_2 = 0