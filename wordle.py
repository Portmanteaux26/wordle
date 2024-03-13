import sys
import random


guess_limit = 6
hint_history = []


def get_guess(raw_guess):
    
    sanitary_guess = raw_guess.lower()

    if len(sanitary_guess) != 5:
        print("The word is 5 letters long.")
    elif sanitary_guess not in guess_set:
        print("That's not a valid word.")
    else:
        return sanitary_guess

def process_guess(guess, solution):
    
    guess_char_count = {}
    solution_char_count = {}
    hint = []

    for i in range(0, 5):
        guess_char_count[guess[i]] = guess_char_count.get(guess[i], 0) + 1
        solution_char_count[solution[i]] = solution_char_count.get(solution[i], 0) + 1
    
    for i in range(0, 5):
        if guess[i] == solution[i]:
            hint += 'O'
            guess_char_count[guess[i]] -= 1
            solution_char_count[solution[i]] -= 1
        elif guess[i] not in solution:
            hint += 'X'
            guess_char_count[guess[i]] -= 1
        else:
            hint += '?'
    
    for i in range(0, 5):
        if hint[i] == 'O':
            continue
        elif guess_char_count[guess[i]] > 0 and solution_char_count[guess[i]] < 1:
            hint[i] = 'X'
            guess_char_count[guess[i]] -= 1
        elif guess_char_count[guess[i]] > 0 and solution_char_count[guess[i]] >= 1:
            guess_char_count[guess[i]] -= 1
            solution_char_count[guess[i]] -= 1
        else:
            guess_char_count[guess[i]] -= 1
    
    return hint


solution_source = open("solutions.txt")
solution_list = solution_source.read().split('\n')
solution_source.close()

solution = random.choice(solution_list)

guess_source = open("guesses.txt")
guess_set = set(guess_source.read().split('\n'))
guess_source.close()

print("""Let's play Wordle.
The word is 5 letters long.
X: Letter not present in word
?: Letter present in word in a different position
O: Correct letter
You have %s guesses.""" % guess_limit)

while guess_limit > 0:
    
    guess = get_guess(input(''))
    
    if guess == None:
        continue
    
    elif guess == solution:
        print("Correct!")
        print('\n'.join(hint_history))
        print("OOOOO")
        exit()

    else:
        guess_limit -= 1
        current_hint = ''.join(process_guess(guess, solution))
        hint_history.append(current_hint)
        if guess_limit > 0:
            print(current_hint)

print("You're out of guesses!  The word was '%s'." % solution)
print('\n'.join(hint_history))