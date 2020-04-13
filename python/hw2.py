# 1.
# Create a function to calculate the "factors" and "factorial" of an int number.

# Examples
#   factors_and_factorial(6) ➞ factors = 1, 2, 3, 6; factorial= 720.
print("Question 1")
def factors_and_factorial(n):
    print("factors = ")
    value = 1
    for x in range(1,n+1):
        if n % x == 0:
            print(x)
        value *= x
        
    print("factorial = {}".format(value))



# factors_and_factorial(5)

# 2.
# Create a function to calculate the mean of all digits.
#   Handle both number and string cases. Convert float number to int number.

# Examples
#   mean(42) ➞ 3
#   mean('12345') ➞ 3
#   mean(666) ➞ 6
#   mean('35.9') ➞ 4
print("Question 2")
def mean_function(n):
    string_int=str(int(float(n)))
    
    value=0
    for character in string_int:
        value += int(character)
    value = value / len(string_int)   
    return(value)
   
    

print(mean_function("633"))


value_int=98544545547654321
reduced_int=value_int

while reduced_int!=0:
    print(reduced_int-reduced_int//10*10)
    reduced_int=reduced_int//10


# Create a function that performs an even-odd transform to a list, n times. Each even-odd transformation:
#     Adds two (+2) to each odd integer.
#     Subtracts two (-2) to each even integer.

# Examples
#   even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
#  Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]
#  
#   even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]
#  
#   even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]

print("Question 3")
def even_odd_transform(list,times):
    for i in range (1, times+1):
        for j in range (len(list)):
            if list[j] % 2 == 0:
                list[j] += 2
            else:
                list[j] -= 2

    return(list)        

print(even_odd_transform([2,3,4],3))

# 4.
# Create a function that takes a string and returns the number 
# (count) of vowels contained within it.

# Examples
#   count_vowels("Celebration") ➞ 5
#   count_vowels("Palm") ➞ 1
#   count_vowels("Prediction") ➞ 4

# Notes
#     a, e, i, o, u are considered vowels (not y).
#     All test cases are one word and only contain letters.

print("Question 4")

def count_vowels(input_string):
    count=0
    for character in input_string:
        if character in ["a","e","i","o","u"]:
            count+=1
    
    return(count)

print(count_vowels("grace"))
    
# 5.
# Additional spaces have been added to a sentence. 
# Return the correct sentence by removing them.
# All words should be separated by one space, 
# and there should be no spaces at the beginning or end of the sentence.

# Examples
#   correct_spacing("The film   starts       at      midnight. ")
#   ➞ "The film starts at midnight."

#   correct_spacing("The     waves were crashing  on the     shore.   ")
#   ➞ "The waves were crashing on the shore."

print("Question 5")

def correct_spacing(input_string):
    output_string=""
    is_first_space = True
    for character in input_string:
        if character != " ":
            output_string += character
            is_first_space = True
        else:
            if is_first_space == True:
                output_string += character
                is_first_space = False 
        
    return(output_string)

print(correct_spacing("hello there Dad.;ikhvI YT3we  "))