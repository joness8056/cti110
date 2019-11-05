# Kilometer Converter
# 11\3\2019
# CTI-110 P5T1_KilometerCOnverter
# STeve Jones
#
#Converts kilometers to miles.
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show main miles function to convert it.
def main ():
    # Get the distance in kilomenters.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles (kilometers)

# The show miles function converts the km from
# kilometers to miles and displays the results.
def show_miles(km):
    #Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equils', miles, 'miles.')

# Call the main function
main()
