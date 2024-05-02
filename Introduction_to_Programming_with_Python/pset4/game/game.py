import random

def main():
    # get level from user
    level = get_level("Level: ")
    # get number to be guess for the level of user
    computer_guess = random.randint(1, level)
    # checking if user guess match
    while True:
        guess = get_guess("Guess: ")
        if guess == computer_guess:
            print("Just right!")
            break
        elif guess < computer_guess:
            print("Too small!")
            continue
        elif guess > computer_guess:
            print("Too large!")
            continue

def get_level(prompt):
    # only positive int reprompt for other
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
            continue
        except ValueError:
            continue

def get_guess(prompt):
    # get the guess only positive int reprompt other
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()