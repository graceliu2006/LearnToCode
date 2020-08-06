from oopgameplayer import Player

tim = Player("Bim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.level = 5
print(tim)

tim.level = 3
print(tim)

tim.level = -2
print(tim)

