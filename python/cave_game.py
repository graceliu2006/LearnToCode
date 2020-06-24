import shelve

cave = shelve.open("cave_game") 

loc = 1
while True:

    exits_list = []
    for short_name in cave["exits"][loc].keys():
        for key, value in cave["full"].items():
            if value == short_name:
                exits_list.append(key)

    #available_exits=", ".join(exits[loc].keys())
    available_exits=", ".join(exits_list)
    print(cave["locations"][loc])

    if loc == 0:
        break
    
    direction = input("Available exits are " + available_exits + ": ").upper()
    print()
    if direction in cave["full"].keys():
        to_convert = cave["full"][direction]
        if to_convert in cave["exits"][loc]:
            loc = cave["exits"][loc][to_convert]
        else:
            print("You cannot go in that direction") 
    else:
            print("This direction does not exist.") 

cave.close()
