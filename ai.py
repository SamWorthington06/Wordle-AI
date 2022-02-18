import random

def get_wordle_guesses():
    words = []
    file = open("wordle_guesses.txt", "r")
    for line in file:
        words.append(line.strip())
    file.close()

    return words

def get_wordle_answers():
    words = []
    file = open("wordle_answers.txt", "r")
    for line in file:
        words.append(line.strip())
    file.close()

    return words


def run():
    guesses = get_wordle_guesses()
    answers = get_wordle_answers()

    answer = random.choice(answers)
    print(answer)

    for guess_counter in range(0,5):
        
        if guess_counter == 0:
            potential_words = ["slate"] #Starter word is SLATE
        else:
            potential_words = guesses

        for guess in potential_words:
            evaluation_of_word_map = {}

            for possible_answer in answers:
                evaluation_of_word = get_evaluation_of_guess(possible_answer, guess)

                if tuple(evaluation_of_word) not in evaluation_of_word_map:
                    evaluation_of_word_map[tuple(evaluation_of_word)] = [possible_answer]
                else:
                    evaluation_of_word_map[tuple(evaluation_of_word)].append(possible_answer)

            possible_remaining_wordcount = max([len(value) for value in evaluation_of_word_map])


def get_evaluation_of_guess(answer, word):
    #0 = nothing, 1 = yellow, 2 = green
    output = [0,0,0,0,0]

    #Correct letter and correct position
    for i in range(0,5):
        if word[i] == answer[i]:
            output[i] = 2
            answer = answer[:i] + ' ' + answer[i+1:]

    #Correct letter and wrong position
    for i in range(0,5):
        char = word[i]
        if char in answer and output[i] == 0:
            output[i] = 1
            first_occurance = answer.find(char)
            answer = answer[:first_occurance] + ' ' + answer[first_occurance + 1:]
    
    return tuple(output)

if __name__ == "__main__":
    run()