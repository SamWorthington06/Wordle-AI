def get_wordle_answers():
    words = []

    file = open("wordle_answers.txt", "r")

    for word in file:
        words.append(word.strip())
    return words

def run():
    first_word = ["slate"]
    print("Please enter the word:",first_word[0].upper())
    
    user_feedback = input("Feedback: ")


if __name__ == "__main__":
    print('''
Enter the feedback of the word
in the following format:

0 = nothing
1 = yellow
2 = green
    ''')

    run()