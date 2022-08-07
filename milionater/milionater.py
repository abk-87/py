def reading_from_file():
    with open('questions.txt', 'r') as f:
        l = f.readlines()
    return l

def choice_of_question(l):
    question = dict()
    i = random.randrange(len(l))
    q = l[i].split('; ')
    for j in range(len(q)):
        segment = q[j].split(': ')
        if j == 1:
            segment[1] = segment[1].split()
        question.update({segment[0]: segment[1]})
    l.remove(l[i])
    return question

def rounds(question, m):
    global b
    
    print(question.get('question'))
    answers = question.get('answers')
    i = random.randrange(len(answers))
    t1 = ('a.', answers[i])
    print(t1[0], t1[1])
    answers.remove(answers[i])
    i = random.randrange(len(answers))
    t2 = ('b.', answers[i])
    print(t2[0], t2[1])
    answers.remove(answers[i])
    i = random.randrange(len(answers))
    t3 = ('c.', answers[i])
    print(t3[0], t3[1])
    answers.remove(answers[i])
    i = random.randrange(len(answers))
    t4 = ('d.', answers[i])
    print(t4[0], t4[1])
    answers.remove(answers[i])
    
    correct_answer = ''
    for j in range(len(question.get('correct')) - 1):
        correct_answer += question.get('correct')[j]
    
    answer = input('Choose an answer: ')
    while answer not in ('a', 'b', 'c', 'd'):
        answer = input('Choose "a", "b", "c" or "d": ')
    for i in t1, t2, t3, t4:
        if answer == i[0][0]:
            if i[1] == correct_answer:
                print('It is the correct answer. You won ' + m + '!\n')
            else:
                print('Your answer is wrong. You lost.')
                b = False
    return b

import random
l = reading_from_file()
round_n = ('1st', '2nd', '3nd')
money_n = ('$100000', '$500000', '$1000000')
n = 0
b = True
print('We are starting the game Who Wants to Be a Millionaire?\n')
while n < 3 and b == True:
    m = money_n[n]
    print(round_n[n], 'question and', m)
    rounds(choice_of_question(l), m)
    n += 1
