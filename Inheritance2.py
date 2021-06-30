class Mammal():
    def __init__(self, name):
        print(name, "is a mammal")
        
class canFly(Mammal):
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")
        
        super().__init__(canFly_name)
        
class canSwim(Mammal):
    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")
        
        super().__init__(canSwim_name)

class Animal(canFly, canSwim):
    def __init__(self, name):
        super().__init__(name)
    
Carol = Animal("Dog")