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
    
    def has_letters(self, word):
        """Checks if the player has the letters for a word
        Sirts the hand and the word, and then checks to see if the letters match
        
        Args:
            word (str): the word thats being checked
        Returns:
            bool: True if hand has the letters for the word, otherwise false
        Author:
            Ou
        """
        temp_hand = sorted(self.hand)
        temp_word = sorted(word.upper())
        
        i = 0
        j = 0
        while i <len(temp_hand) and j < len(temp_word):
            if temp_hand[i] == temp_word[j]:
                j += 1
            i += 1
        return j == len(temp_word)
        

#class for the die
class Die:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        pass
    
class ConsonantDie(Die):
    def __init__(self):
        """Initializes a ConsonantDie object. Inherits from the Die class.
        Author: 
            Buitrago.
        """
        super().__init__(["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"])

class VowelDie(Die):
    def __init__(self):
        """Initializes a VowelDie object. Inherits from the Die class.
        Author:
            Buitrago.
        """
        super().__init__(["A", "E", "I", "O", "U"])
        

#Scoring
class ScoringSystem:
    def __init__(self):
        """Creates the scoring system
        Author:
            Ou
        """
        self.letter_values = {
            #These values are from scrabble and we can change them
            "A": 1, "E": 1, "I": 1, "O": 1, "U": 1,
            "L": 1, "N": 1, "S": 1, "T": 1, "R": 1,
            "D": 2, "G": 2,
            "B": 3, "C": 3, "M": 3, "P": 3,
            "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
            "K": 5,
            "J": 8, "X": 8,
            "Q": 10, "Z": 10
        }
    def length_multiplier(self,word):
        """Gets the score multiplier
        words with 7 or more letters get x2, 5-7 is x1.5, else is 1
        Args:
            word (str): the word for scoring
        Returns:
            float: The score multiplier
        Author:
            Ou
        """
        
        if len(word) >= 7:
            return 2
        elif len(word) >= 5:
            return 1.5
        else:
            return 1
    def calculate_word(self, word):
        """Calculates the score for a word
        Args:
            word (str): the word for scoring
        Returns:
            int: the points to be earned from the word(score)
        Author:
            Ou
        """
        word = word.upper()
        base_score = 0
        for letter in word:
            base_score += self.letter_values.get(letter, 0)
        mult = self.get_length_multiplier(word)
        return int(base_score * mult)
    
        
    
    def calculate_turn_score(self, words):
        """calculates score for the turn
        Algorithm skeleton
        """
        total_score = 0
    
        #1 loop through word
        #2 calculate score total based on letter values
        #3 length multiplier
        #4 add calculated turn score to total
        pass
    

class Game:
    def __init__(self):
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
        """Initializes a WordManager object and word bank attribute.
        Returns:
            An instance of a WordManager object. 
        Author:
            Buitrago.
        """
        self.bank = pd.read_csv('word_bank.csv')
        self.bank = self.bank[self.bank['word'].str.len() >= 3]

    def isInWordBank(self, word):
        """Checks to see if a player's word is in the word bank.
        Args: 
            word (str): the word to be checked.
        Returns:
            True if the word is in the word bank, False otherwise. 
        Author:
            Buitrago.
        """
        words = self.bank[self.bank['word'].str.upper() == word.upper()]
        return len(words) > 0
    
    def submit_word(self, player, word):
        """Checks if a player's word is valid and they have the letters for it
        Args:
            player (Player): The player submitting the word
            word (str): The word being submitted
        Returns:
            True if the word is valid and playable by player, otherwise it is false
        Author:
            Ou
        """
        
        if not self.is_in_word_bank(word):
            return False
        if not player.has_letters_for(word):
            return False
        return True

    
            
        
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

# creating rounds 

for number in rounds
    rounds = 10
    
    print("ROUND START")
    
    # Player 1 turn
    input("\n" + name_1 + ", press Enter to Play!")


# Calculate who won 
if score_1 > score_2:
    print(name_1, "WINS!!")
    
if score_2 > score_1:
    print(name_2, "WINS!!")

if score_1 == score_2:
    print("IT'S A TIE!")

