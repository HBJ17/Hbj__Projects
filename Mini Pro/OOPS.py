class car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model
    
    def show_details(self):
        print(f"Car : {self.brand} , {self.model}")

car1 = car("Scoda","Rapid")
car2 = car("Audi","A30")

car1.show_details()
car2.show_details()







