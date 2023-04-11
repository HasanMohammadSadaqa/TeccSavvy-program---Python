"""The project involves building a quiz game that reads questions and answers from a text file, presents the
questions to the user, and checks if the answers are correct"""

user_score = {}
question_and_answer = {}


def receive_user_information():
    """
    :return:username
    """
    user_name = input("Enter your name please: ")
    user_score[user_name] = 0
    return user_name


def start_quiz():
    """
    start the quiz by calling the receive_user_info() function to get the username and then calls the ask_question()
    and get_user_score() functions to ask questions and update the user score.
    """
    user_name = receive_user_information()
    read_question()
    read_answer()
    print(user_score)
    print(question_and_answer)


def read_question():
    """
    it's a function to read the questions and choices from the file
    """
    counter = 0
    try:
        with open("question.txt", "r") as qfile:
            for line in qfile.readlines():
                if line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                    question_and_answer[counter]["choices"].append(line.strip())
                else:
                    counter += 1
                    question_and_answer[counter] = {
                        "question": line.strip(), "choices": [], "answer": ""
                    }
    except FileNotFoundError:
        print("'question.txt' not found")
        start_quiz()


def read_answer():
    """
    it's a function reads the answer from a file
    """
    counter = 0
    try:
        with open("answers.txt", "r") as afile:
            for line in afile.readlines():
                counter += 1
                question_and_answer[counter]["answer"] = line.strip()
    except FileNotFoundError:
        print("'answer.txt' not found")
        start_quiz()


if __name__ == '__main__':
    start_quiz()
