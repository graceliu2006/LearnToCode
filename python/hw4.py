print("Question 1")
# 1.
# Create a function that determines whether a number is Oddish or Evenish. 
# A number is Oddish if the sum of all of its digits is odd, 
# and a number is Evenish if the sum of all of its digits is even. 
# If a number is Oddish, return "Oddish". Otherwise, return "Evenish".

# For example, oddish_or_evenish(121) should return "Evenish", 
# since 1 + 2 + 1 = 4. 
# oddish_or_evenish(41) should return "Oddish", since 4 + 1 = 5.

# Examples
#   oddish_or_evenish(43) ➞ "Oddish"
#   oddish_or_evenish(373) ➞ "Oddish"
#   oddish_or_evenish(4433) ➞ "Evenish"

def oddish_or_evenish(number):
    
    number_string = str(number)
    digit_sum = 0
    for digit in number_string:
        digit_sum += int(digit)
    if digit_sum % 2 == 0:
        return("Evenish")
    else:
        return("Oddish")

def another_oddish_or_evenish(number):
    digit_sum = 0
    
    rounded = number
    while rounded != 0:
        last_digit = rounded % 10
        rounded = rounded // 10
        digit_sum += last_digit
    
    if digit_sum % 2 == 0:
        return("Evenish")
    else:
        return("Oddish")
   
print(another_oddish_or_evenish(373))

print("Question 2")

# 2. In each input list, every number repeats at least once, except for two.
# Write a function that returns the two unique numbers.

# Examples
#   returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
#   returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
#   returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]

def unique(list):
    frequency_table={}
    unique = []
    
    for i in list:
        if i in frequency_table:
            frequency_table[i] += 1
        else: 
            frequency_table[i] = 1

    for i in frequency_table:
        if frequency_table[i] == 1:
            unique.append(i)
    return(unique)

           
    
def another_unique(list):
    history = [0,0,0,0,0,0,0,0,0,0]
    unique = []
    
    for i in list:
        history[i] += 1
    print(history)    

    for i in range(len(history)):
        if history[i] == 1:
            unique.append(i)
    return(unique)
           


print(unique([1, 9, 8, 8, 7, 6, 1, 6, 124, 43, "dog", "dog", "cute dog"]))

print("Question 3")
# 3. You work for a manufacturer, and have been asked to calculate the 
# total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), 
# sell price per unit (in dollars), and the starting inventory. 
# Return the total profit made, rounded to the nearest dollar. 
# Assume all of the inventory has been sold.

# Examples

# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796

# profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# }) ➞ 32411

# profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# }) ➞ 44030

def profit(prices):
    
    raw_profit = (prices["sell"] - prices["cost"]) * prices["inventory"]
    total_profit = int(((raw_profit)*100)//100)
    return(raw_profit,total_profit)

print(profit({"cost": 2.77, "sell": 7.95, "inventory": 8500
}))

print("Question 4")

# 4. A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 
# distinct solutions for real values of x. 
# Given a, b and c, you should return the number of solutions to the equation.

# Examples
#   solutions(1, 0, -1) ➞ 2
#     // x² - 1 = 0 has two solutions (x = 1 and x = -1).
#   solutions(1, 0, 0) ➞ 1
#     // x² = 0 has one solution (x = 0).
#   solutions(1, 0, 1) ➞ 0
#     // x² + 1 = 0 has no solutions.

# Notes
#   "a" will always be non-zero.

def solutions(a,b,c):
    discriminant = (b ** 2) - 4 * a * c
    if discriminant > 0:
        return("2")
    elif discriminant == 0:
        return("1")
    else:
        return("0")

print(solutions(1, 0, 1))

print("Question 5")
# 5.
# Write a Python program to read lines from a file and save them to another file with reverse order.

with open("jabberwocky.txt", 'r') as jabber:
    with open("homework4p5.txt",'w') as reverse:
        lines = jabber.readlines()

        print(lines[0])
        for line in lines[::-1]:
            print(line, end= '', file=reverse)










