# Wordle (Single Player & Battle Mode)
## Description

## Features
- **Single Player Mode:** Play against the AI in a challenge to uncover the hidden word first.
- **Battle Mode:** Compete directly with the AI, taking turns to guess the word.
- **Scoring System:** AI uses a dynamic scoring system to make educated guesses based on previous feedback.
- **Interactive Interface:** Simple text-based interface for inputting guesses and receiving feedback.

## Installation
To run this game, you will need Python installed on your computer. The game is compatible with Python 3.6 and above. No additional libraries are required to run the base version of the game.

1. Install Python from python.org
2. Download the source code for the game from the repository or copy it into a local file.

## How to Run
To start the game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the game files.
3. Run the command python main.py to start the game.
4. Follow the on-screen prompts to choose between Single Player Mode or Battle Mode.

## How to Play
- **Start the Game:** Choose your mode and start the game through the menu system.
- **Guessing:** Input your guess for the five-letter word. The game will provide feedback in the form of colored tiles:
  - 🟩 Green: Correct letter in the correct position.
  - 🟨 Yellow: Correct letter in the wrong position.
  - ⬛ Black: Incorrect letter.
- **AI Turn:** The AI will make a guess based on its scoring system and previous feedback.
- **Winning the Game:** The game continues until either the player or the AI guesses the word, or both run out of attempts.

## Limitations
- The AI's guessing efficiency depends on the complexity and diversity of the word list.
- Currently supports only five-letter words.
- No graphical user interface; the game runs in the command line.
