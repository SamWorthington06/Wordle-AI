'''
Wordle AI solver
@author - Sam Worthington
'''

def get_wordle_guesses():
    '''
    Reads a file containing all the possible wordle guesses
    @return - returns a list of all possible wordle guesses
    '''
    words = []

    file = open("wordle_guesses.txt", "r")

    for word in file:
        words.append(word.strip())
    file.close()
    return words

def get_wordle_answers():
    '''
    Reads a file containing all the possible wordle answers
    @return - returns a list of all possible wordle answers
    '''
    words = []

    file = open("wordle_answers.txt", "r")

    for word in file:
        words.append(word.strip())
    file.close()
    return words

def run():
    '''
    Solves your wordle problem by the user giving feedback after each attempted guess
    '''
    guesses = get_wordle_guesses()
    answers = get_wordle_answers()
    guess_this_word = ""
    
    #We want to minimise the 'answers' list after each guess
    #Set to a number higher than the number of words in starting list
    minimum_number_of_words = 15000
    
    evaluation_of_answers_dict = {}

    #6 attempts to guess the word
    for attempt in range(6):
        if attempt > 0:
            potential_words = guesses
        else:
            potential_words = ["slate"]

        #Loops through all the potential guesses
        for guess in potential_words:
            temp_evaluation_of_answers_dict = {}
            
            #Loops through all the potential answers evaluating the feedback to each guess word
            for answer in answers:
                feedback = get_evaluation_of_guess(answer, guess)
                tp_feedback = tuple(feedback)

                #Checks to see if the evaluated feedback (e.g. (1, 2, 0, 2, 1)) is in the answers dictionary
                if tp_feedback not in temp_evaluation_of_answers_dict:
                    temp_evaluation_of_answers_dict[tp_feedback] = [answer]
                else:
                    temp_evaluation_of_answers_dict[tp_feedback].append(answer)

            #We want to minimise this variable to be more likely to find the answer
            maximum_number_of_words = max([len(value) for value in temp_evaluation_of_answers_dict.values()])
            
            if maximum_number_of_words < minimum_number_of_words:
                minimum_number_of_words = maximum_number_of_words
                guess_this_word = guess

                evaluation_of_answers_dict = temp_evaluation_of_answers_dict

        print("Please enter the word:",guess_this_word.upper())
        guess_evaluation = give_feedback()

        #Updates the potential list of answers
        if guess_evaluation in evaluation_of_answers_dict:
            answers = evaluation_of_answers_dict[guess_evaluation]

        #If there is only one word left, it must be the answer
        if len(answers) == 1:
            print("\nAnswer:",answers[0].upper())
            break

def get_evaluation_of_guess(answer, word):
    '''
    This function returns the evaluation of the words stored in 'answer' and 'word'
    @param - answer - is a word from the list of answers
    @param - word - is a word from the list of guesses
    @return - returns an evaluation of the parameters in a tuple format (e.g. '(1, 2, 0, 2, 1)')
    '''
    #Feedback: 0 = nothing; 1 = in word, wrong position; 2 = in word, correct position;
    feedback = [0, 0, 0, 0, 0]
    
    #Check if letter is in the word and in the correct position
    for index in range(5):
        if word[index] == answer[index]:
            feedback[index] = 2
            answer = answer[:index] + ' ' + answer[index + 1:]
           
    #Check if letter is in the word
    for index in range(5):
        letter = word[index]
        if letter in answer and feedback[index] == 0:
            feedback[index] = 1
            first_occurence = answer.find(letter)
            answer = answer[:first_occurence] + ' ' + answer[first_occurence + 1:]
    
    return tuple(feedback)

def give_feedback():
    '''
    This function gets the user's feedback after each guess
    @return - the user's feedback in tuple form (e.g. (1, 2, 0, 2, 1))
    '''
    user_feedback = input("Feedback: ")

    if len(user_feedback) != 5:
        print("5 digits only. Try again\n")
        give_feedback()
    else:
        feedback = []
        for i in range(5):
            feedback.append(int(user_feedback[i]))

    return tuple(feedback)

if __name__ == "__main__":
    print('''
Enter the feedback of the word
in the following format:

0 = nothing
1 = yellow
2 = green
''')

    run()