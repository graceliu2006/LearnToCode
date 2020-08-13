from oopgameenemy import Enemy, TimBuchalka, Vampire, VampireKing

tim1 = TimBuchalka("TheOriginalTim")
print("Tim Buchalka - {}".format(tim1))


tim1.identify()
tim1.take_damage(3)
print("Tim Buchalka - {}".format(tim1))


vampire1 = Vampire("Vlad")
# print("Vlad - {}".format(vampire1))

# vampire1.identify()
# vampire1.take_damage(3)
# print("Vlad - {}".format(vampire1))


print(vampire1)

while vampire1._alive:
    vampire1.take_damage(1)
        
print(vampire1)

vampireking1 = VampireKing("Boris")
print(vampireking1)
vampireking1.take_damage(1)
print(vampireking1)

