# Math Quiz
# 11-4-2019
# CTI-110 P5HW2 - Math Quiz
# Steve Jones
#
# Give simple math quzzes by displaying two
# random numbers.
# Allow students to enter answer.
# Message of congradulations if correct.
# show correct answer if wrong.

import random 
def menu():
    print('1. Add Random Numbers')
    print('2. Subtract Random Numbers')
    print('3. Exit')
 
        
Student = random.randint(1,2)
number1 = random.randint(1,500)
number2 = random.randint(1,500)
if Student == 1:
    
    print('Calculate', number1, '+', number2)
    answer = number1 + number2

elif Student == 2:
    
    print('Calculate', number1, '-', number2)
    answer = number1 - number2
    
student_answer = int(input())
if student_answer == answer:
    print('CONGRADULATIONS!!!')
    
    
