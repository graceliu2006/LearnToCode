def choices_function(option_list):
    chosen = ""

    print("Please choose your option from the list below:")
    i=1

    for option in option_list:
        print(str(i) + ". " + option)
        i += 1
    print("0. exit")

    while chosen != 0:
        chosen = int(input("Please choose an option: "))
        #if chosen in range (0,len(option_list)+1):
        if chosen in range (0,i):
            print("You chose option {}".format(chosen))
            

choices_function(["sleep","nap","slumber","snooze","doze","siesta","hibernate"])