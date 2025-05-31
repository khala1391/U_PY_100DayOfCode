class Animal:
    def __init__(self):
        self.num_eyes= 2
    
    def breath(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breath(self):
        super().breath()
        print("doing this unterwater")
    
    
    
    def swim(self):
        print("moving in the water.")

nemo = Fish()
nemo.swim()
nemo.breath()


