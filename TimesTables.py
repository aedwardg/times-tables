"""
This program was designed to help my son learn and memorize his multiplication.
It is a simple terminal game that provides user with multiplication problems
from the times tables 0 through 12.

All suggestions for improving functions or readability welcome.

"""

import os
import random
import time
from time import sleep


base_list = list(range(13))
number_names = [
    'zeros', 'ones', 'twos', 'threes', 'fours', 'fives', 'sixes',
    'sevens', 'eights', 'nines', 'tens', 'elevens', 'twelves'
    ]
n = 0
final_score = 0
running_tallies = []
points_possible = []


# Primary function
def multiply(numbers):
    score = 0
    for number in numbers:
        product = base_list[n] * number
        answer = input('What is {} x {}? '.format(base_list[n], number))
        try:
            if int(answer) == product:
                score += 1
                print ('Correct!')
                sleep(1)
                clear()
            else:
                print('Incorrect!  {} x {} is: '.format(base_list[n], number))
                print(product)
                sleep(2)
                clear()
        except:
            print('Incorrect!  {} x {} is: '.format(base_list[n], number))
            print(product)
            sleep(2)
            clear()

    running_tallies.append(score)
    points_possible.append(13)
    get_score = 'You got %s out of 13 right.' % (score)
    print(get_score)
    if n < 12:
        keep_playing()
    else:
        total_score(final_score)
        raise SystemExit

# Continue practicing times tables
def keep_playing():
    play = input('Do you want to keep playing? ')
    play = play.upper()
    if play == 'YES':
        global n 
        n += 1
        print ("Great, here we go! Let's practice your %s!" % number_names[n])
        print('\n')
        sleep(2)
        multiply(base_list)
    else:
        print ('Thanks for playing!')
        print('\n')
        total_score(final_score)
        raise SystemExit

# Multiplication test with 20 random questions betweens ones and twelves
def test():
    score = 0
    for i in range(20):
        points_possible.append(1)
        test_q = [random.randint(1, 12), random.randint(1, 12)]
        product = test_q[0] * test_q[1]
        answer = input('What is {} x {}? '.format(test_q[0], test_q[1]))

        try:
            if int(answer) == product:
                score += 1
                print ('Correct!')
                sleep(1)
                clear()
            else:
                print('Incorrect!  {} x {} is: '.format(test_q[0], test_q[1]))
                print(product)
                sleep(2)
                clear()
        except:
            print('Incorrect!  {} x {} is: '.format(test_q[0], test_q[1]))
            print(product)
            sleep(2)
            clear()

    running_tallies.append(score)
    total_score(final_score)
    raise SystemExit

# function calculating final score after game is completed
def total_score(tally):
    current_time = time.time()
    time_elapsed = current_time - start_time
    tally = final_score + sum(running_tallies)
    print('Congratulations! You exercised your brain for {0} minutes and {1} seconds!'.format(
        round(time_elapsed/60, 0),
        round(time_elapsed % 60, 2)
        ))
    print('Your final score is: %s points.' % (tally))
    print('Points possible: %s' % (sum(points_possible)))
    letter_grade = tally / sum(points_possible)

    if letter_grade >= 0.9:
        print('Letter grade: A')
    elif letter_grade >= 0.8:
        print('Letter grade: B')
    elif letter_grade >= 0.7:
        print('Letter grade: C')
    elif letter_grade >= 0.6:
        print ('Letter grade: D')
    else:
        print ('Letter grade: F')

# Function to clear screen
def clear():
    os.system('cls||clear')    


# Introduction and begin zeros
print('Hi, welcome to my classroom! My name is Ms. Multi Ply, or Ms. Ply for short.')
sleep(2)
print('I will be your teacher today.')
sleep(2)
name = input('What is your name? ')
print('Hello, %s!' % (name))
sleep(2)
print('Do you want to practice your times tables or take a test?')
practice_test = input('Type PRACTICE, TEST or EXIT ')
practice_test = practice_test.upper()
if practice_test == 'PRACTICE':
    print ("Okay! Let's start with zeros.")
    sleep(2)
    start_time = time.time()
    multiply(base_list)
    keep_playing()
elif practice_test == 'TEST':
    start_time = time.time()
    test()
else:
    print ('Okay, goodbye!')
    raise SystemExit
