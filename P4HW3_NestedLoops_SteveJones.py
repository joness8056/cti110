# Write a program that uses nested loops to draw a pattern with #
# October 17, 2019
# CTI-110 P4HW3 - Nested Loops
# Steve Jones



# Display a pattern with number signs stepping out at
# Display six rows of # signs
# Example:##
          # #
          #  #
          #   #
          #    #
          #     # 


# Code to display example above  
NUM_STEPS = 6

for r in range(NUM_STEPS):
    print('#' , end='',)
    for soace in range(r):
        print(' ' , end='')
    print('#')
        
  

    
