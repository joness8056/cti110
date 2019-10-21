# Total number of bugs collected 
# October 17, 2019
# CTI-110 P4T2 - Bug Collector
# Steve Jones


# set total=0
# for each of 5 days
# bugs collected per day
# total bugs collected
# Show Total

total  = 0

#bugs collected for each day
for day in range(1, 6):

    # user input
    print('Enter bugs collected on day', day)

    # number of bugs
    bugs = int(input())

    # Add bugs for total
    total = total + bugs

#Show total bugs 
print('You collected a total of', total, 'bugs.')
