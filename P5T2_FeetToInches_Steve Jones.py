# Feet to Inches Conversion Code
# Date
# CTI-110 P5T2_FeetToInches
# Steve Jones
#

#COnverts for the number of the inches per foog.
INCHES_PER_FOOT = 12

#main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
          
# The feet to inches function converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()
