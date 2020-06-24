import shelve

cave = shelve.open("cave_game") 
cave["locations"] = {0: "You are sitting in front of a computer learning Python",
                    1: "You are standing at the end of a road before a small brick building",
                    2: "You are at the top of a hill",
                    3: "You are inside a building, a well house for a small stream",
                    4: "You are in a valley beside a stream",
                    5: "You are in the forest"}
cave["exits"] = {0:{"Q": 0},      #list of dictionaries with directions from each location
                1:{"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                2:{"N":5, "Q": 0},
                3:{"W": 1, "Q": 0},
                4:{"N": 1, "W": 2, "Q": 0},
                5:{"W": 2, "S": 1, "Q": 0}}

cave["full"] = {"NORTH": "N",
            "EAST": "E", 
            "SOUTH": "S",
            "WEST": "W",
            "QUIT": "Q"}

# print(cave["locations"])

for i in cave:
    print(cave[i])
cave.close()
