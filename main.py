import random

# TODO: Make it so when a letter is used and it isn't in the word it will be removed from the list of possible letters
# TODO: Make it so you can only guess words that are in the list of words
# TODO: Make a battle mode to go against either an AI or another player
# TODO: Make a main menu to choose between the two modes

def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

words = load_words('wordle-words.txt')

# Choose a random word from the list
answer = random.choice(words)

# Checks if the guess is correct
def check_guess(guess, answer):
    result = []
    for i in range(len(guess)):
        if guess[i] == answer[i]: 
            # If the letter is in the correct position and is correct the letter will turn green
            result.append('🟩') 
        elif guess[i] in answer:
            # If the letter is in the word but not in the correct position the letter will turn yellow
            result.append('🟨')
        else:
            # If the letter is not in the word the letter will turn red
            result.append('⬛')
    return result

def main():
    print("Welcome to Wordle!")
    print("Guess the five letter word.")
    attempts = 6
    while attempts > 0:
        guess = input("Enter a 5-letter word: ").strip().lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        print(check_guess(guess, answer))
        if guess == answer:
            print("Congratulations! You've guessed the word.")
            break
        attempts -= 1
    else:
        print("You've run out of attempts. The word was:", answer)

main()