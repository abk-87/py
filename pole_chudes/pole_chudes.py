def reading_from_file():
    with open('questions.txt', 'r') as f:
        l = f.readlines()
        for i in range(len(l)):
            l[i] = l[i][:-1]
    return l

def choice_of_questions(l):
    i = random.randrange(len(l))
    question_1 = l[i].split(': ')
    l.remove(l[i])
    i = random.randrange(len(l))
    question_2 = l[i].split(': ')
    l.remove(l[i])
    i = random.randrange(len(l))
    question_3 = l[i].split(': ')
    l.remove(l[i])
    questions = (question_1, question_2, question_3)
    return questions

import random
questions = choice_of_questions(reading_from_file())
print('\nWELCOME TO THE GAME "FIELD OF WONDERS". WISH YOU GOOD LUCK!\n')
for i in range(len(questions)):
    print('\t\tQuestion N', i+1, '\n')
    print(questions[i][0])
    answer = ('*' * len(questions[i][1]))
    print(answer)
    while answer != questions[i][1]:
        letter = input('\nPlease guess a letter: ')
        if not letter:
            continue
        elif len(letter) > 1:
            print('You must typed only 1 letter')
            continue
        elif 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            if letter.upper() in answer:
                print('You already guessed this letter')
                continue
            if letter.upper() in questions[i][1]:
                print('It\'s right, there is the letter "', letter, '" in the answer!', sep='')
                for j in range(len(answer)):
                    if letter.upper() == questions[i][1][j]:
                        answer = answer[:j] + letter.upper() + answer[j+1:]
                print(answer)
            else:
                print('No, there isn\'t the letter "', letter, '" in the answer.', sep='')
        else:
            print('It isn\'t a letter.')
    print('\nWELL DONE!\n')
print('CONGRATS, YOU WIN!!!')
