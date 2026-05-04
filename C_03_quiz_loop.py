num_questions = get_integer("How many questions do you want? ")

while num_questions <= 0:
    print("Please enter a number greater than 0.")
    num_questions = get_integer("How many questions do you want? ")