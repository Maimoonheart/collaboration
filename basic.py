print('Welcome to collaboration class.')

def square(x):
    return x **5
print(square(4))

"""
working on object car
types
method:details(Bukunmi)
method:drive(Pelumi)
method:drift(Boluwatife)
method:park(Ayodele)
method:reverse(Toluwanimi)
method:ignition(Maimunah)
"""
class Cars():
    tyre = 4
    engine=1
    bonnet = 1
    brake = 1
    accelerator = 1
    def __init__(self,color,make,model,year,price,engine_type) -> None:
        self.color = color 
        self.maker = make
        self.model= model
        self.year = year
        self.price = price
        self.engine_type = engine_type
