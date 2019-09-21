# Calculator for your Meal, Tip, and Tax
# September 20, 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Steve Jones
#
meal = float(input ("How much did your meal cost?"))
total_cost = meal + (meal * 0.06) + (meal * 0.30)

print("You total meal cost is:$ %.2f" % total_cost)
