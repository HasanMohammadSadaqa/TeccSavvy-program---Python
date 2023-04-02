story = "Once upon a time, there was a adjective1 noun who loved to verb in the adjective2 noun2."
print("Welcome to the Mad Libs Game!\n")
while True:

    print("Please enter the following: ")
    adjective1 = input("-An adjective: ")
    noun1 = input("-A noun: ")
    verb1 = input("-A verb: ")
    adjective2 = input("-Another Adjective: ")
    noun2 = input("-Another noun: ")
    inputs_error = []
    # adjective 1
    if adjective1.isdigit() or adjective2.isdigit():
        inputs_error.append("Adjective must be letters only")
    if not adjective1.isalpha() or not adjective2.isalpha():
        inputs_error.append("Adjective must be letters only")
    # noun
    if noun1.isdigit() or noun2.isdigit():
        inputs_error.append("Noun must be letters only")
    if not noun1.isalpha() or not noun2.isalpha():
        inputs_error.append("Noun must be letters only")

    while len(inputs_error) > 0:
        for error in inputs_error:
            print(error)
            print("__________________________________")
        break
    else:
        completed_story = story.replace("adjective1", adjective1).replace("noun", noun1).replace("verb", verb1).replace("adjective2", adjective2).replace("noun2", noun2)


