import random

def gen():
    x = random.randint(1, len(options)) #Implies that the 0th index is 1
    options = dict(1 ="Ketchup and Mustard Only", 2="Pickles, lots and lots of pickles", 
        3="Peanut Butter and Jelly", 4="Pepperoni, Spinach, BBQ Sauce, and Mayonaise", 
            5="lots of salt and maple syrup for your popcorn pancakes")
    #Dict type to store all possible options
    return options[x]

gen() #Immediate closure

