# 11.24

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.



def sum_list(l):
    i = 0
    for x in l:
        i = i + x
    return i







print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134



# 11.25

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.


def measure_udacity(l):
    i = 0
    for x in l:
        if x[0] == 'U':
            i = i + 1
    return i


#print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

#print measure_udacity(['Umika','Umberto'])
#>>> 2



# 11.26

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(l,v):
    i = -1
    for x in range(0,len(l)):
        if l[x] == v:
            i = x
            break
    return i



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1



# 11.29

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.



def union(x,y):
    for i in y:
        if i not in x:
            x.append(i)
    return x


# To test, uncomment all lines
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]
