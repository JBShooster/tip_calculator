#tip calculator v2
#This version of Tip Calculator uses raw input supplied from the user.

meal = float(raw_input("What is the cost of your meal? (e.g., 15.80): "))
tax = float(raw_input("Enter the tax rate as a decimal (e.g., .07, not 7%): "))
tip = float(raw_input("What percent tip do you want to leave? Enter as decimal (e.g., .15): "))

tax_value = meal * tax
meal_with_tax = tax_value + meal
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print("\n\nThe base cost of your meal is ${0:.2f}. ".format(meal))
print("Your tax value is ${0:.2f}. ".format(tax_value))
print("If you tip at a rate of {0:.2f}%, you ought to leave ${1:.2f} as a tip.".format(int(tip*100), tip_value)) 
print("Your meal total is ${0:.2f}. ".format(total))

raw_input("\n\n Press any key to exit...")
