class Kettle(object):

    power_source = "electricity"
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False 

    def switch_on(self): 
        self.on = True

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)


kenwood.price = 12.75
print(kenwood.price)

iroh = Kettle("Uncle Iroh's Teaware", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, iroh.make, iroh.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, iroh))

print(iroh.on)
iroh.switch_on()
print(iroh.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)
kenwood.power = 1.5
print(kenwood.power)
print("Switch to firebending")
Kettle.power_source = "firebending"
print(Kettle.power_source)
print("switch kenwood to airbending")
kenwood.power_source = "airbending"
print(kenwood.power_source)
print(iroh.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(iroh.__dict__)

