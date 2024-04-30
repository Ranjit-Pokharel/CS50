def main():
    # get user math problem
    text = input("Expression: ")
    # interprete the problem
    answer = interpreter(text)
    # display answer
    print(answer)

def interpreter(text):
    # get number and operators
    num1, operator, num2 = text.strip().split()
    num1 = float(num1)
    num2 = float(num2)
    # match the operator
    match operator:
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2


if __name__ == "__main__":
    main()