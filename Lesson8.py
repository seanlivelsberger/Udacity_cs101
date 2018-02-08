# 8.1

# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: #
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    i = 0
    while i < len(product):
        if debris.find(product[i]) >= 0:
            i = i + 1
        else:
            break
    if i == len(product):
        return product
    else:
        return "Give me something that's not useless next time."

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'



# 8.2

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def date_increment(year,month,day):
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 > 0) and month == 2 and day == 28:
        return year,month,29
    elif year % 4 == 0 and not (year % 100 == 0 and year % 400 > 0) and month == 2 and day == 29:
        return year,month+1,1
    elif month == 2 and day == 28:
        return year,month+1,1
    elif month == 12 and day == 31:
        return year+1,1,1
    elif month in [9,4,6,11] and day == 30:
        return year,month+1,1
    elif day == 31:
        return year,month+1,1
    else:
        return year,month,day+1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    i = 0
    while year1 != year2 or month1 != month2 or day1 != day2:
        year1,month1,day1 = date_increment(year1,month1,day1)
        i = i + 1
    return i



# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()



# 8.4

# By AnnaGajdova from forums
# You are in the middle of a jungle.
# Suddenly you see an animal coming to you.
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!"
#            If you are not: "Stay calm and wait!".
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal,
# that takes as input a string and a number,
# an animal and your speed (in km/h),
# and prints out what to do.

def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    if animal == 'zebra':
        print "Try to ride a zebra!"
    elif animal == 'cheetah' and my_speed > 115:
        print "Run!"
    elif animal == 'cheetah':
        print "Stay calm and wait!"
    else:
        print "Introduce yourself!"


jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"
