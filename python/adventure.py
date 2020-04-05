exits = ["north", "south", "east", "west"]

chosen = ""
while chosen not in exits:
    chosen = input("Please choose a direction: ").casefold()
    if chosen == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")
