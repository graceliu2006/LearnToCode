name =  input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

# if age >= 18:
#     print("You're old enough to leave home and never come back to your 3 point dad. Congratulations!!!!!!!!")
#     print("Please put an L in the box")   
# else:
#     print("Don't worry, you can escape in {0} years".format(18-age)) 

if age <18: 
    print("Don't worry, you can escape in {0} years".format(18-age))     
elif age == 327:
        print("You are the legendary Cheesebreath Senior. Your legacy is one of violence, malevolence, and")
else: 
    print("You're old enough to leave home and never come back to your -1 point dad. Congratulations!!!!!!!!")
    print("Please put an L in the box")

