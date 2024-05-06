import random

# Load words from a file into a list
def load_words(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

# List of words to choose from
words = load_words('wordle-words.txt')

# Choose a random word from the list
answer = random.choice(words)

# Checks if the guess is correct and returns result
def check_guess(guess, answer):
    guess = guess.lower() 
    answer = answer.lower()
    letter_result = list(guess.upper())  # return the uppercase version of the guess
    color_result = ['⬛'] * len(guess) # initialize all letters to black
    answer_counts = {}

    # Count occurrences of each letter in the answer
    for letter in answer:
        if letter in answer_counts:
            answer_counts[letter] += 1
        else:
            answer_counts[letter] = 1

    # First pass to mark greens (correct letter and position)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            color_result[i] = '🟩'
            answer_counts[guess[i]] -= 1

    # Second pass to mark yellows (correct letter but wrong position)
    for i in range(len(guess)):
        if guess[i] != answer[i] and guess[i] in answer_counts and answer_counts[guess[i]] > 0:
            if color_result[i] == '⬛':
                color_result[i] = '🟨'
                answer_counts[guess[i]] -= 1

    return letter_result, color_result

# Single player mode functionality
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

# Two player mode functionality
# Initializes the players scores for two player mode
def initialize_players():
    return {'Player 1': 0, 'Player 2': 0}

# switch_turn function to switch between players
def switch_turn(player):
    players = ('Player 1', 'Player 2')
    return players[(players.index(player) + 1) % len(players)]

# Displays the scores of the players
def display_score(scores):
    print("\nScores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

# Two Player mode: each player guesses an assigned random word
def two_player():
    players = initialize_players()
    current_turn = 'Player 1'
    words_to_guess = {'Player 1': random.choice(words), 'Player 2': random.choice(words)}
    attempts_left = {'Player 1': 6, 'Player 2': 6}

    while attempts_left['Player 1'] > 0 or attempts_left['Player 2'] > 0:
        opponent = switch_turn(current_turn)
        opponent_word = words_to_guess[opponent]

        if attempts_left[current_turn] > 0:
            print(f"\n{current_turn}'s turn to guess.")
            guess = input(f"Attempt {7 - attempts_left[current_turn]}/6: Enter your guess: ").strip().lower()
            while len(guess) != 5 or guess not in words:
                guess = input("Invalid guess! Enter a valid 5-letter word: ").strip().lower()

            color_result, letter_result = check_guess(guess, opponent_word)
            print(letter_result, color_result)

            if guess == opponent_word:
                print(f"Correct! {current_turn} guessed the word!")
                players[current_turn] += 1
                break
            else:
                attempts_left[current_turn] -= 1

        current_turn = switch_turn(current_turn)

    for player in ['Player 1', 'Player 2']:
        if attempts_left[player] == 0:
            print(f"\nOut of attempts for {player}! The correct word was: {words_to_guess[player]}")

    display_score(players)

    if input("Play another round? (y/n): ").strip().lower() != 'y':
        print("\nFinal Scores:")
        display_score(players)
    else:
        two_player()

# Implementing Battle mode functionality
# AI implementation
# Initializes the letter possibilities (whether its in the word or not, and whether position is correct) to the AI logic to determine the word
def initialize_ai_constraints(word_length):
    # ⬛
    not_in_word = []
    # 🟨
    in_word_wrong_position = []
    for _ in range(word_length):
        in_word_wrong_position.append([])
    # 🟩
    in_word_correct_position = [None] * word_length
    return not_in_word, in_word_wrong_position, in_word_correct_position

# updates the AI constraints based on the guess and color result
def update_ai_constraints(guess, color_result, not_in_word, in_word_wrong_position, in_word_correct_position, answer):
    guess = guess.lower()
    answer = answer.lower()
    letter_count = {}  # assuming this dictionary tracks the counts of letters

    # Initialize letter_count dictionary with all letters from the answer
    for letter in answer:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

    # Update constraints based on the guess and color_result
    for i in range(len(guess)):
        if color_result[i] == '🟩':
            if guess[i] in letter_count:
                letter_count[guess[i]] -= 1
                if letter_count[guess[i]] == 0:
                    del letter_count[guess[i]]
            in_word_correct_position[i] = guess[i]
        elif color_result[i] == '🟨':
            if guess[i] in letter_count:
                letter_count[guess[i]] -= 1
                if letter_count[guess[i]] == 0:
                    del letter_count[guess[i]]
            in_word_wrong_position[i].append(guess[i])
        elif color_result[i] == '⬛':
            not_in_word.append(guess[i])

# scores the word based on the constraints and returns the score of the word
def score_word(word, not_in_word, in_word_wrong_position, in_word_correct_position):
    score = 0
    i = 0

    # Score green positions
    for letter in in_word_correct_position:
        if letter:
            if word[i] == letter:
                score += 3  # High score for correct position
            else:
                score -= 1  # Penalty for not using a known correct letter in this position
        i += 1

    # Check for previously identified not-in-word letters
    for letter in not_in_word:
        if letter in word:
            score -= 2  # Penalty for including a letter known not to be in the word

    # Score yellow positions: correct letter but should be in different position
    i = 0
    for letters in in_word_wrong_position:
        for letter in letters:
            if letter in word:
                if word[i] != letter:
                    score += 1  # Moderate score for correct letter in different position
                else:
                    score -= 1  # Penalty for placing a yellow letter in the same position
        i += 1

    return score

# guesses the word based on the constraints and returns the best guess
def ai_guess(words, not_in_word, in_word_wrong_position, in_word_correct_position):
    max_score = float('-inf')
    best_guess = None

    for word in words:
        score = score_word(word, not_in_word, in_word_wrong_position, in_word_correct_position)
        if score > max_score:
            max_score = score
            best_guess = word

    return best_guess if best_guess else random.choice(words)  # Fallback to a random choice if no best guess is found

# Battle mode functionality
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
            print("Player's Guess:", ' '.join(player_letter_result))
            print("Player's Feedback:", ' '.join(player_color_result))

            if player_guess == player_answer:
                print("Congratulations! You have guessed the word correctly!")
                break
            player_attempts -= 1

        if ai_attempts > 0:
            print("\nAI's Turn:")
            ai_guess_word = ai_guess(words, not_in_word, in_word_wrong_position, in_word_correct_position)
            if ai_guess_word:
                ai_guess_word = ai_guess_word.upper()
                ai_letter_result, ai_color_result = check_guess(ai_guess_word, ai_answer)
                print("AI's guess:", ' '.join(ai_guess_word))
                print("AI's Feedback:", ' '.join(ai_color_result))
                update_ai_constraints(ai_guess_word, ai_color_result, not_in_word, in_word_wrong_position, in_word_correct_position, ai_answer)
                if ''.join(ai_letter_result) == ai_answer.upper():
                    print("\nAI has guessed the word correctly!")
                    print("AI wins! The correct word was:", ai_answer)
                    print("Player's word was:", player_answer)
                    break
            ai_attempts -= 1

    if player_attempts == 0 and ai_attempts == 0:
        print("Both player and AI have run out of attempts. The words were:", player_answer, ai_answer)
    elif player_attempts == 0:
        print("Player has run out of attempts. The AI's word was:", ai_answer)
    elif ai_attempts == 0:
        print("AI has run out of attempts. The player's word was:", player_answer)

# Main menu to choose the mode     
def menu():
    print("Welcome to Wordle!")
    print("1. Single Player Mode")
    print("2. Two Player Mode")
    print("3. Battle Mode")
    print("4. Rules")

    choice = input("Choose a mode: ")
    if choice == "1" or choice.lower() == "single player mode":
        single_player()
    elif choice == "2" or choice.lower() == "two player mode":
        two_player()
    elif choice == "3" or choice.lower() == "battle mode":
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