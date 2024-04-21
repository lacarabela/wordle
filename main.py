import random

def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

words = load_words('wordle-words.txt')

# Choose a random word from the list
answer = random.choice(words)

# Checks if the guess is correct
def check_guess(guess, answer):
    letter_result = []
    color_result = []
    for i in range(len(guess)):
        if guess[i] == answer[i]: 
            letter_result.append(guess[i].upper())
            # If the letter is in the correct position and is correct the letter will turn green
            color_result.append('🟩') 
        elif guess[i] in answer:
            letter_result.append(guess[i].upper())
            # If the letter is in the word but not in the correct position the letter will turn yellow
            color_result.append('🟨')
        else:
            letter_result.append(guess[i].upper())
            # If the letter is not in the word the letter will turn grey
            color_result.append('⬛')
    return letter_result, color_result

def single_player():
    print("Guess the five letter word.")
    attempts = 6
    while attempts > 0:
        guess = input("Enter a 5-letter word: ").strip().lower()
        
        # Makes sure the guess is 5 letters and is in the list of words
        if len(guess) != 5 or guess not in words:
            print("Invalid guess or not in dictionary. Try again.")
            continue

        print(check_guess(guess, answer))

        if guess == answer:
            print("Congratulations! You've guessed the word.")
            break
        attempts -= 1
    else:
        print("You've run out of attempts. The word was:", answer)

# AI implementation

def initialize_ai_constraints(word_length):
    not_in_word = []
    in_word_wrong_position = []
    for _ in range(word_length):
        in_word_wrong_position.append([])
    in_word_correct_position = [None] * word_length
    return not_in_word, in_word_wrong_position, in_word_correct_position

def update_ai_constraints(guess, feedback, not_in_word, in_word_wrong_position, in_word_correct_position):
    word_length = len(guess)
    for i in range(word_length):
        if feedback[i] == '⬛':
            not_in_word.append(guess[i])
        elif feedback[i] == '🟨':
            in_word_wrong_position[i].append(guess[i])
        elif feedback[i] == '🟩':
            in_word_correct_position[i] = guess[i]

def ai_guess(words, not_in_word, in_word_wrong_position, in_word_correct_position):
    possible_words = []
    for word in words:
        validity = True

        for i in range(len(word)):
            if word[i] in not_in_word:
                validity = False
                break
            if word[i] in in_word_wrong_position[i]:
                validity = False
                break
            if in_word_correct_position[i] is not None and word[i] != in_word_correct_position[i]:
                validity = False
                break
        
        if validity:
            possible_words.append(word)
        
    return random.choice(possible_words)

def battle_mode():
    player_answer = random.choice(words)
    ai_answer = random.choice(words)

    not_in_word, in_word_wrong_position, in_word_correct_position = initialize_ai_constraints(len(ai_answer))

    player_attempts = 6
    ai_attempts = 6

    while player_attempts > 0 or ai_attempts > 0:
        if player_attempts > 0:
            print("\nPlayer's turn:")
            player_guess = input("Enter a 5-letter word: ").strip().lower()
            if len(player_guess) != 5 or player_guess not in words:
                print("Invalid guess or not in dictionary. Try again.")
                continue

            player_letter_result, player_color_result = check_guess(player_guess, player_answer)
            print('Letters:', ' '.join(player_letter_result))
            print('Feedback:', ' '.join(player_color_result))

            if player_guess == player_answer:
                print("Congratulations! You have guessed the word correctly!")
                break
            player_attempts -= 1

        if ai_attempts > 0:
            print("\nAI's Turn:")
            ai_guess_word = ai_guess(words, not_in_word, in_word_wrong_position, in_word_correct_position)
            if ai_guess_word:
                ai_letter_result, ai_color_result = check_guess(ai_guess_word, ai_answer)
                print("AI's guess:", ai_guess_word)
                print("AI's Feedback:", ' '.join(ai_color_result))
                update_ai_constraints(ai_guess_word, ai_color_result, not_in_word, in_word_wrong_position, in_word_correct_position)
                if ai_guess == ai_answer:
                    print("AI has guessed the word correctly!")
                    break
            ai_attempts -= 1

    if player_attempts == 0 and ai_attempts == 0:
        print("Both player and AI have run out of attempts. The words were:", player_answer, ai_answer)
    elif player_attempts == 0:
        print("Player has run out of attempts. The AI's word was:", ai_answer)
    elif ai_attempts == 0:
        print("AI has run out of attempts. The player's word was:", player_answer)
        
def menu():
    print("Welcome to Wordle!")
    print("1. Single Player Mode")
    print("2. Battle Mode")
    print("3. Rules")

    choice = input("Choose a mode: ")
    if choice == "1" or choice.lower() == "single player mode":
        single_player()
    elif choice == "2" or choice.lower() == "battle mode":
        battle_mode()
    elif choice == "3" or choice.lower() == "rules":
        print("The goal of the game is to guess the word in 6 attempts.")
        print("If the letter is in the correct position and is correct the letter will turn green.")
        print("If the letter is in the word but not in the correct position the letter will turn yellow.")
        print("If the letter is not in the word the letter will turn grey.")
        menu()
    else:
        print("Invalid choice. Try again.")
        menu()

menu()