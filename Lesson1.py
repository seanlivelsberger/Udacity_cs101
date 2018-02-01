# 1.7

# This is a Python comment. Lines that begin with a '#' are ignored by the
# Python interpreter. Comments are useful for documenting code or explaining
# quiz questions!
#
# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result
#
# Click the "Test Run" button below to try running your code and see the output,
# and click "Submit" to submit your answer.

print (60 * 24 * 7 * 7)



# 1.14

# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print (299792458 * 100 * 1.0/1000000000)



# 1.18

# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print (speed_of_light / cycles_per_second)



# 1.22

# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.

age = 26
print 26 * 365



# 1.26

# Define a variable, name, and assign to it a string that is your name.

name = 'sean'



# 1.31

# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.

s = 'audacity'

print 'U' + s[2:8]



# 1.40



# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url',
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')

url = page[start_link + 9: page.find('"',start_link + 9)]

print url
