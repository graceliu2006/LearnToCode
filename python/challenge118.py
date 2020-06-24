import shelve

# books = shelve.open("book")
# books["recipes"] = {"blt": ["bacon","lettuce","tomato","bread"],
#                     "beans_on_toast": ["beans","bread"],
#                     "scrambled eggs": ["eggs","butter","milk"],
#                     "soup":["tin of soup"],
#                     "pasta":["pasta","cheese"]}
# books["maintenance"] = {"stuck": ["oil"],
#                     "loose": ["gaffer tape"]}

# print(books["recipes"])
# # print(books["recipes"]["scrambled eggs"])

# # print(books["maintenance"]["loose"])
# books.close()

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0:{"Q": 0},      #list of dictionaries with directions from each location
         1:{"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2:{"N":5, "Q": 0},
         3:{"W": 1, "Q": 0},
         4:{"N": 1, "W": 2, "Q": 0},
         5:{"W": 2, "S": 1, "Q": 0}}

full = {"NORTH": "N",
        "EAST": "E", 
        "SOUTH": "S",
        "WEST": "W",
        "QUIT": "Q"}

loc = 1
while True:

    exits_list = []
    for short_name in exits[loc].keys():
        for key, value in full.items():
            if value == short_name:
                exits_list.append(key)

    #available_exits=", ".join(exits[loc].keys())
    available_exits=", ".join(exits_list)
    print(locations[loc])

    if loc == 0:
        break
    
    direction = input("Available exits are " + available_exits + ": ").upper()
    print()
    if direction in full.keys():
        to_convert = full[direction]
        if to_convert in exits[loc]:
            loc = exits[loc][to_convert]
        else:
            print("You cannot go in that direction") 
    else:
            print("This direction does not exist.") 


