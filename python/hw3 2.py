# 1.
# Create a function to calculate the "max", "min", and "mean" of a list.

# Examples
#   max_min_mean([6,1,5,3,4,2]) ➞ max = 6; min = 1; mean = 3.5.

print("Question 1")
def calculate(numbers):
    max = numbers[0]
    min = numbers[0]
    sum = 0

    for i in numbers:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    mean = float(sum) / len(numbers)

    return(max , min , mean)

my_list=[9,6,-4]
print(calculate(my_list))

# 2.
# Given an unsorted list, create a function that returns the 
# nth smallest element (the smallest element is the first smallest, 
# the second smallest element is the second smallest, etc).
# Examples
#   nth_smallest([1, 3, 5, 7], 1) ➞ 1
#   nth_smallest([1, 3, 5, 7], 3) ➞ 5
#   nth_smallest([1, 3, 5, 7], 5) ➞ None
#   nth_smallest([7, 3, 5, 1], 2) ➞ 3


print("Question 2")

def nth_smallest(elements,n):
    ordered = (sorted(elements))
    if n > len(ordered):
        print("None")
    else:
        print(ordered[n-1])
    
my_list2 = [3,1,2,5,4]
nth_smallest(my_list2,5)

# 3.
# Write a function that takes a list and a number as arguments. 
# Add the number to the end of the list, 
# then remove the first element of the list. 
# The function should then return the updated list.

# Examples
#   next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
#   next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
#   next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
#   next_in_line([], 6) ➞ "No list has been selected"

# Notes
#   For an empty list input, return: "No list has been selected"

print("Question 3")

def queue(list,last):
    if len(list) > 0:
        del(list[0])
        list.append(last)
        print(list)
    else:
        print("No list has been selected")
    
queue_list = [1,2,3,4,5]
queue(queue_list,6)

# 4.
# Create a function that takes a list of numbers between x1 and x2 
# and returns the missing numbers.
#   Case 1 : Only one number will be missing.
#   Case 2 : More than one number will be missing.

# Examples (assume x1=1, and x2=10)
#   missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
#   missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
#   missing_num([10, 5, 1, 2, 6, 8, 3, 9]) ➞ 4, 7

# Notes
#     The list of numbers will be unsorted (not in order).

print("Question 4")
def missing(list,min,max):
    for l in range(min,max+1):
        if l not in list:
            print(l)

    
missing_list = [1,3,2,4,6,5,9,8,10]
missing(missing_list,1,10)

# 5.
# Given two lines, determine whether or not they are parallel.
# Lines are represented by a list [a, b, c], 
# which corresponds to the line ax+by=c.

# Examples
#   lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ true
#     # x+2y=3 and x+2y=4 are parallel.
#   lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ false
#     # 2x+4y=1 and 4x+2y=1 are not parallel.
#   lines_are_parallel([0, 1, 5], [0, 2, 15]) ➞ true
#     # Lines are parallel to x axis.

# Notes
#     All the test cases use valid input (so no lists of the wrong size, for example).
#     All the coefficients will be integers (whole numbers).
#     Coefficients can be 0.

#slope = -a/b

print("Question 5")
def parallel(line1,line2):
    are_parallel = False
    if line1[1] != 0  and line2[1] != 0:
        if (line1[0] * -1) / line1[1] == (line2[0] * -1) / line2[1]:
            are_parallel = True
    else:
        if line1[1] == line2[1]:
            are_parallel = True
    
    return(are_parallel)

line1 =[0,4,3]
line2 = [0,1,4]
print(parallel(line1 , line2))

# 6. AMC8 2017 Problem 20
# An integer between 1000 and 9999, inclusive, is chosen at random. 
# How may ways that it is an odd integer whose digits are all distinct? 
print("Question 6")

def odd_distinct():
    distinct = 0
    for integer in range(1000,10000):
        converted = str(integer)
        
        count = [0,0,0,0,0,0,0,0,0,0]
        for i in converted:
            count[int(i)] += 1

        unique = True
        for i in count:
            if i>1:
                unique = False
        if unique == True and int(integer) % 2 == 1:
            distinct += 1
    return(distinct)   

print(odd_distinct())