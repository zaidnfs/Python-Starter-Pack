
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

# print(add(1,2,3,4,5,6))

def calculator(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(kwargs["multiply"])

# calculator(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seat = kw.get("seat")
        self.colour = kw.get("colour")

my_car = Car(make="Supra", colour="Yellow")
print(my_car.make, my_car.colour)