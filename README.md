# Wordle (Single Player, Two Player & Battle Mode) - INST126 
## Description
This Wordle AI game is a text-based version of the popular word puzzle game, featuring two distinct gameplay modes: Single Player Mode and Battle Mode. In Single Player Mode, players try to guess a hidden five-letter word based on feedback, mimicking the classic gameplay popularized by the New York Times. In Battle Mode, players compete against an AI opponent that improves its guesses based on feedback from its initial guess and subsequent scoring of potential words. The game utilizes a text file containing a bank of five-letter words as its source for word selection, ensuring a diverse and challenging experience with each session.

## Features
- **Single Player Mode:** Play the standard NYT Worlde until you grow tired of it!
- **Two Player Mode:** Play against a friend in a battle to see who will figure out their mystery word first.
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
4. Follow the on-screen prompts to choose between Single Player Mode, Two Player mode or Battle Mode.

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
