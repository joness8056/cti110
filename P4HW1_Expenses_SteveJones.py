# Expense Calculator
# CTI-110
# P4HW1 - Expenses
# Steve Jones
# October 17, 2019

# Enter amount in account and expences.
# Enter expense
# calculate total
# would user like to add another expense?
# if no, total amount before expense
# numbers of expenses
# total after expenses


keep_going = 'y'
print = 'total'

while keep_going =='y':

    amount = float(input('Enter the amount in account: '))
    expenses = float(input('Enter your expense: '))

    total = amount - expenses

    keep_going = input('Add another expense ' +
                       'total (Enter y for yes(: ')
    Print('The total is $',
          format(total, ',.2f'), sep='')
    


    
    




    



