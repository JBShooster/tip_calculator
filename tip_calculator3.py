#Tip Calculator V3
#This version of Tip Calculator imports the script args.py and uses the variables
#from the list args as inputs for meal, tip, and tax

from args import args

 
meal = float(args[0])
tip = float(args[1])
tax = float(args[2])
 
tax_value = meal * tax
meal_with_tax = tax_value + meal
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value
 
print "The base cost of your meal was ${0:.2f}.".format(meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
                                                        int(100*tip), tip_value)

 
print "The grand total of your meal is ${0:.2f}.".format(total)

raw_input('\n\n Press any key to exit...')
