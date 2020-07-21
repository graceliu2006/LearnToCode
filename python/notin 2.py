# activity = input("What would you like to do today? ")

# if "cinema" not in activity.casefold():
#     print("But I want to go to the cinema")

name = input("What is your name? ")
age_string = input("What is your age? ")

if name!="" and age_string!="":
    if 18 <= int(age_string) < 31:
        print("Welcome to the holiday," + name)
    else:
        print("Go away! Nobody wants you here, " + name)
else:
    print("Please enter an input.")