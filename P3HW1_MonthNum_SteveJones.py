# CTI-110
# P3HW1 - Month number
# Steve Jones
# September 30, 2019
    
# Enter month number 1 through 12
# Display the name of the month by number entered
# error message outside of numbers 1 through 12

month_lst = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December']
try:
    month = int(input('Enter the number to be converted: '))
    if month < 1 or month > 12:
        raise ValueError
    else:
        print(month_lst[month - 1])
except ValueError:
    print("Invalid number")
