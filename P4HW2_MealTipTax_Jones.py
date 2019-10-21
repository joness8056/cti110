# CTI-110
# P4HW2 - MealTipTax
# Steve Jones 
# October 17, 2019

# Enter charge for meal
# Add tip of only 16%, 18%, or 20%
# Add tip a second time of only 16%, 18%, or 20%
# add 6% sales tax
# Total of all 



meal_cost = float(input("What is the total cost of the meal? >>> "))
tip_percent = int(input("How much tip did you want to include? >>> 16% or 18% or 20%? "))
tip_percent = int(input("How much tip did you want to include? >>> 16% or 18% or 20%? "))
tax = 0.06

# Ask user if they'd like to run the program again and enter another tip
another = 'y' 

while another == 'y':
    another = input('Enter again? ' + ' (Enter y for yes): ')
    meal_cost = float(input("What is the total cost of the meal? >>> "))
    tip_percent = int(input("How much tip did you want to include? >>> 16% or 18% or 20%? "))
    tip_percent = int(input("How much tip did you want to include? >>> 16% or 18% or 20%? "))
    tax = 0.06 
        
 
def meal_calculator(meal_cost, tip_percent):
    meal_plus_tax = float(meal_cost) * float(1 + tax)
    tip_amount = float(meal_plus_tax*tip_percent/100)
    
 
    print("- -- "*15)
 
    print("Meal Cost: $%0.2f\n"
          "Tax: %0.4f%%\n"
          "Total(excluding tip): $%0.2f\n"
          "Suggested tip at %%%d: $%0.2f\n"
          %(meal_cost, tax, meal_plus_tax, tip_percent, tip_amount))
 
    print("Have an awesome day! Thank you.")
    print("- -- "*15)
 
meal_calculator(meal_cost, tip_percent)
