with open("question.txt", "r") as file:
    content = file.readlines()
    content[0].strip()
    print(content[0])