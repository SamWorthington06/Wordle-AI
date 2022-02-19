def get_wordle_guesses():
    words = []

    file = open("wordle_guesses.txt", "r")

    for word in file:
        words.append(word.strip())
    return words

def get_wordle_answers():
    words = []

    file = open("wordle_answers.txt", "r")

    for word in file:
        words.append(word.strip())
    return words

def run():
    guesses = get_wordle_guesses()
    answers = get_wordle_answers()
    

    evaluation_of_answers = {}
    min_wordcount = 1e6
    chosen_word = ""

    #6 attempts to guess the word
    for guess in range(6):
        if guess > 0:
            potential_words = guesses
        else:
            potential_words = ["slate"]

        for guess in guesses:
            temp_evaluation_dict = {}

        

    if len(answers) == 1:
        print("Answer should be:",answers)


def give_feedback():
    user_feedback = input("Feedback: ")

    if len(user_feedback) != 5:
        print("5 digits only. Try again\n")
        give_feedback()
    else:
        feedback = []
        for i in range(5):
            feedback.append(user_feedback[i])

    return feedback

if __name__ == "__main__":
    print('''
Enter the feedback of the word
in the following format:

0 = nothing
1 = yellow
2 = green

Please enter the word: SLATE
    ''')

    run()