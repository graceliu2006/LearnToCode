print("Question 1")

# 1.
# Create a function that creates a box based on dimension n.

# Examples

# makeBox(5, '#') ➞ [
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]

# makeBox(3, '*') ➞ [
#   "***",
#   "* *",
#   "***"
# ]

# makeBox(2, '@') ➞ [
#   "@@",
#   "@@"
# ]

# makeBox(1, '&') ➞ [
#   "&"
# ]
import time
def make_box(dimension, symbol):

    print(symbol*dimension)
    for i in range(dimension - 2):
        print(symbol + (" " * (dimension - 2)) + symbol)
    if dimension >= 2:
        print(symbol*dimension)
start_time = time.time()
make_box(2,"@")
print(time.time()-start_time)
print("Question 2")
# 2.
# In this challenge, you have to establish if a given integer n is a Sastry number. 
# If the number resulting from the concatenation of an integer n 
# with its successor is a perfect square, then n is a Sastry Number.

# Given a positive integer n, 
# implement a function that returns True if n is a Sastry number, 
# or False if it's not.

# Examples
#   is_sastry(183) ➞ True
#     # Concatenation of n and its successor = 183184
#     # 183184 is a perfect square (428 ^ 2)
#   is_sastry(184) ➞ False
#     # Concatenation of n and its successor = 184185
#     # 184185 is not a perfect square
#   is_sastry(106755) ➞ True
#     # Concatenation of n and its successor = 106755106756
#     # 106755106756 is a perfect square (326734 ^ 2)

# Notes
#   You can expect only valid positive integers greater than 0 as input, 
# without exceptions to handle. Zero is a perfect square, 
# but the concatenation 00 isn't considered as a valid result to check.
import math
def is_sastry(number):
    sastrified = int(str(number) + str(number+1))
    sqrt = math.sqrt(sastrified)
    return sqrt - int(sqrt) == 0

i=1
while not is_sastry(i):
    i=i+1 

print(i)

print("Question 3")

# 3.
# Make a function that encrypts a given input with these steps:

# Input: "apple"

# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
#           a => 0
#           e => 1
#           o => 2
#           u => 3
#         # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"

# Output: "1lpp0aca"

# Examples
#   encrypt("banana") ➞ "0n0n0baca"
#   encrypt("karaca") ➞ "0c0r0kaca"
#   encrypt("burak") ➞ "k0r3baca"
#   encrypt("alpaca") ➞ "0c0pl0aca"

# Notes
#   All inputs are strings, no uppercases and all output must be strings.

def encrypt(string):
    vowels = ["a","e","o","u"]
    #{a:0,e:1,o:2,u:3}
    encoded = ""

    reversed = string[::-1]
    for letter in reversed:
        if letter in vowels:
            encoded += str(vowels.index(letter))
        else: 
            encoded += letter
    encoded += "aca"
    print(encoded)
start_time = time.time()
encrypt("banana")
print(time.time()-start_time)
print("Question 4")

# 4.
# Make a function to decrypt the output from above HW3.

def unscramble(string):
    
    vowels = {"0":"a","1":"e","2":"o","3":"u"}
    removed = string[:-3]
    decoded = ""
    
    print(removed)
    for char in removed:
        if char in vowels.keys():
            decoded += vowels[char]
        else: 
            decoded += char
    print(decoded)        
    
    reversed = decoded[::-1]
    print(reversed)
start_time = time.time()   
unscramble("0n0n0baca")
print(time.time()-start_time)
print("Question 5")

# 5. Use time modul to measure the running time of above 4 functions.

