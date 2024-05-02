import random


def main():
    # list of questions with there answer
    questions_answers = {}
    # get the level for user
    level = get_level()
    # get random 2 numbers
    while True:
        x = generate_integer(level)
        y = generate_integer(level)
        # update the question and there answer to the list
        questions_answers[f"{x} + {y}"] = x + y
        # if theere is 10 question exit loop
        if len(questions_answers) == 10:
            break

    # get only questions from the list
    questions = questions_answers.keys()
    # initial score is 0
    score = 0

    # loop over questions
    for question in questions:
        # initial try 3
        hearts = 3
        while True:
            # if try reduce to 0 show answer and go to next question
            if hearts == 0:
                print(f"{question} = {questions_answers[question]}")
                break

            # get the answer from user
            try:
                answer = int(input(question + " = "))
            except ValueError:
                # if answer is other then int decrease try
                print("EEE")
                hearts -= 1
                continue
            else:
                # if answer doesnot match decrease try
                if answer != questions_answers[question]:
                    print("EEE")
                    hearts -= 1
                    continue
                else:
                    # otherwise answer is correct increase score
                    score += 1
                    break

    # display score
    print(f"Score: {score}")

def get_level():
    # get int
    while True:
        try:
            n = int(input("Level: "))
            # valid only positive int and only 3 level 1, 2, and 3
            if n in [1, 2, 3] and n > 0:
                return n
            continue
        except ValueError:
            continue


def generate_integer(level):
    # level setup
    levels = {"1" : {"start":0, "end": 9}, "2" : {"start":10, "end": 99}, "3" : {"start":100, "end": 999}}
    level = levels[str(level)]
    # get random int with help of level
    x = random.randint(level["start"], level["end"])
    return x

if __name__ == "__main__":
    main()