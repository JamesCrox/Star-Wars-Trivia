from questions import quiz
import pyfiglet


def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False

def print_dictionary():
    """
    Prints out all questions and answers at the end of the app.
    """
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print(pyfiglet.figlet_format("Welcome To", justify="center"))
    print(pyfiglet.figlet_format("Star Wars Trivia\n", justify="center"))
    name = input("What is your name?\n")
    print(f"Hi {name}, Welcome to the star wars trivia game!")    
    print("There are a total of 20 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start the fun ;)\n")
    return True

intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

input("Press enter to see your score ;)\n")
print(f"Your final score is {score}!\n\n")
input("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()
print(pyfiglet.figlet_format("Thanks for playing!"))
