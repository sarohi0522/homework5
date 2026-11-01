class Vehicle:
    def __init__(self, brand, base_fare):
        self.brand = brand
        self.base_fare = base_fare

    def calculate_fare(self):
        return self.base_fare

class Bus(Vehicle):
    def __init__(self, brand, base_fare, capacity):
        super().__init__(brand, base_fare)  
        self.capacity = capacity

    def calculate_fare(self):
        return self.base_fare * 1.10  
my_bus = Bus("Volvo", 50, 40)
print(f"Bus Fare: ${my_bus.calculate_fare()}")
print(f"Is Bus a subclass of Vehicle?: {issubclass(Bus, Vehicle)}")
