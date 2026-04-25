# Wordsmith Game

## Game Description

**Wordsmith** is a word-building game where players use randomly rolled letter dice to form valid English words and earn points based on letter values and word length. The game combines elements of classic word games like Scrabble with dice-rolling mechanics for dynamic gameplay.

### How to Play
- Players take turns rolling consonant and vowel dice to build their hand of available letters
- Each turn, players attempt to form valid English words using letters from their hand
- Words are validated against an internal word bank (minimum 3 letters)
- Points are awarded based on:
  - **Letter Values**: Each letter has a point value (inspired by Scrabble scoring)
  - **Length Multiplier**: Words with 7+ letters earn 2x points, 5-6 letters earn 1.5x points, shorter words earn 1x points
- The game runs for 10 rounds, and the player with the highest total score wins

### Game Features
- Dice-based letter generation (consonant and vowel dice)
- Comprehensive word validation using a curated word bank (~1,000 words)
- Dynamic scoring system with letter weights and length bonuses
- Support for multiple players
- Round-based turn structure

---

## File Descriptions

### `wordsmith.py` (Main Game File)
The primary Python file containing all game logic and classes:

- **`Player` Class**: Represents a game player
  - `__init__(name)`: Initializes a player with a name, score, and hand
  - `add_letter(letter)`: Adds a letter to the player's hand
  - `has_letters(word)`: Checks if the player's current hand contains all letters needed for a word using a two-pointer sorting algorithm

- **`Die` Class**: Base class for letter dice
  - `__init__(sides)`: Initializes a die with possible sides/values
  - `roll()`: Returns a random letter from the die's available letters

- **`ConsonantDie` Class**: Inherits from `Die`, contains 21 consonants (B-Z, excluding vowels)
- **`VowelDie` Class**: Inherits from `Die`, contains 5 vowels (A, E, I, O, U)

- **`ScoringSystem` Class**: Manages game scoring
  - `letter_values`: Dictionary mapping each letter to its point value (based on Scrabble scoring)
  - `length_multiplier(word)`: Returns a multiplier based on word length:
    - 7+ letters: 2x multiplier
    - 5-6 letters: 1.5x multiplier
    - Less than 5: 1x multiplier
  - `calculate_word(word)`: Computes the score for a single word by summing letter values and applying the length multiplier
  - `calculate_turn_score(words)`: Aggregates scores for all words submitted in a single turn (skeleton implementation)

- **`WordManager` Class**: Handles word validation and game dictionary
  - `__init__()`: Loads a CSV word bank and filters words with 3+ letters using Pandas
  - `isInWordBank(word)`: Case-insensitive search to verify if a word exists in the word bank
  - `submit_word(player, word)`: Validates both word existence and whether the player has the required letters

- **`Game` Class**: Core game controller (skeleton implementation)
  - `setup_players()`: Initializes players at game start
  - `play_turn()`: Manages a single player's turn
  - `play()`: Main game loop

- **`main()` Function**: Entry point for game execution

### `word_bank.csv`
A CSV file containing approximately 1,000 common English words used for game word validation. The word bank includes:
- Words of varying lengths (filtered to 3+ letters minimum)
- Common vocabulary words from basic English word lists
- Sourced from publicly available word lists

**File format**: Single column named "word" with one word per row

### Supporting Data
Game constants and configuration (at the bottom of `wordsmith.py`):
- `WELCOME_TO_MY_WORDSMITH_GAME`: Game title display
- `total_rounds`: Set to 10 rounds per game
- `score_1`, `score_2`: Player score tracking variables (to be integrated into `Player` class)

---

## Annotated Bibliography

### Data Sources

**1. Random English Word List (Source: Public Word Bank)**
- **URL/Source**: Common English word list (sourced from online word database)
- **Purpose**: Used as the basis for creating `word_bank.csv`, containing ~1,000 common English words for game validation
- **Application**: The `WordManager` class filters and searches this word bank to validate player-submitted words. The Pandas library filters the dataset to include only words with 3 or more letters, reducing the word bank from 1,000 to 972 valid words.

### Python Programming Sources

**2. Pandas DataFrame Filtering and Queries**
- **Source**: Pandas Official Documentation - "Indexing and Selecting Data"
- **URL**: https://pandas.pydata.org/docs/user_guide/indexing.html
- **Purpose**: Learned string filtering methods for CSV manipulation
- **Application**: Used in `WordManager.__init__()` with `bank[bank['word'].str.len() >= 3]` to filter words by length. Also used in `isInWordBank()` with `bank[bank['word'].str.upper() == word.upper()]` for case-insensitive word lookups. This pandas filtering satisfied one of the project's Python library requirements.

**3. Object-Oriented Programming in Python - Inheritance**
- **Source**: Python Official Documentation - "Classes"
- **URL**: https://docs.python.org/3/tutorial/classes.html
- **Purpose**: Understanding class inheritance and the super() method
- **Application**: Used to create `ConsonantDie` and `VowelDie` as subclasses of the base `Die` class using `super().__init__()` to call the parent constructor, demonstrating inheritance and polymorphism principles.

**4. Sorting and Two-Pointer Algorithm**
- **Source**: Common algorithmic patterns for string matching
- **Purpose**: Efficient method to check if a player's hand contains all letters for a word
- **Application**: In `Player.has_letters()`, both the player's hand and the target word are sorted, then two pointers iterate through both sequences in parallel to check letter availability. This approach runs in O(n log n) time due to sorting, which is more efficient than repeated lookups.

**5. Python Dictionary Methods**
- **Source**: Python Official Documentation - "Dictionaries"
- **URL**: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- **Purpose**: Using dictionaries for key-value pair storage
- **Application**: The `ScoringSystem.letter_values` dictionary maps each letter to its Scrabble-based point value. The `calculate_word()` method uses `.get(letter, 0)` to safely retrieve letter values with a default of 0 for unknown letters.

**6. Scrabble Letter Point Values**
- **Source**: Official Scrabble Rules and Scoring
- **URL**: https://scrabble.hasbro.com/ (Scrabble Official Rules)
- **Purpose**: Authentic point values for word game scoring
- **Application**: The `ScoringSystem.letter_values` dictionary uses official Scrabble scoring as a foundation (A=1, Q=10, Z=10, etc.), providing balanced and recognizable game mechanics for players familiar with classic word games.

### Project Background Sources

**7. Word Games - Game Design Principles**
- **Source**: Common knowledge about word games (Scrabble, Wordle, Boggle)
- **Purpose**: Understand game mechanics and player experience
- **Application**: Informed the design of the multiplier system (favoring longer words) and the combination of dice rolls with word validation, creating engaging gameplay that balances luck (dice rolls) with skill (word knowledge).

---

## Technical Summary

- **Language**: Python 3
- **Key Libraries**: 
  - `pandas` (data manipulation and CSV filtering)
  - `random` (dice rolling mechanics)
- **Data Structure**: CSV-based word bank with Pandas DataFrame filtering
- **Design Patterns**: Object-oriented programming with inheritance, encapsulation, and modular class design
- **Status**: In active development (skeleton methods to be completed)

---

## Future Development

The following components are currently skeleton implementations and require completion:
- `Die.roll()`: Implement random selection from available letters
- `Player.add_letter()`: Implement letter addition to player hand
- `Game.setup_players()`: Initialize players based on user input
- `Game.play_turn()`: Implement turn logic with word submission and scoring
- `Game.play()`: Implement 10-round game loop
- `ScoringSystem.calculate_turn_score()`: Implement aggregate scoring for multiple words

---

## How to Run

```bash
python wordsmith.py
```

Ensure that `word_bank.csv` is in the same directory as `wordsmith.py`.
