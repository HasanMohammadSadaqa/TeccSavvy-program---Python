
story = "Once upon a noun, there was a adjective noun who loved to verb."

noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")


completed_story = story.replace("noun", noun1).replace("adjective", adjective1).replace("noun", noun2).replace("verb", verb1)


print(completed_story)