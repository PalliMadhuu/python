# Base Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model}: Engine starts with a generic sound."

    def stop_engine(self):
        return f"{self.brand} {self.model}: Engine stops."


# Single Inheritance
class Car(Vehicle):
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)
        self.num_of_doors = num_of_doors

    # Method overriding
    def start_engine(self):
        base = super().start_engine()
        return base + f" This car has {self.num_of_doors} doors and goes Vroom!"

    def open_trunk(self):
        return f"{self.brand} {self.model}'s trunk is now open."


# Another base class for multiple inheritance
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity  # in kWh

    def charge(self):
        return f"Charging battery ({self.battery_capacity} kWh)... Done!"

    def vehicle_type(self):
        return "Electric Vehicle"


# Multiple Inheritance
class ElectricCar(Car, Electric):
    def __init__(self, brand, model, num_of_doors, battery_capacity):
        Car.__init__(self, brand, model, num_of_doors)
        Electric.__init__(self, battery_capacity)

    # Overriding method with unique behavior
    def start_engine(self):
        return f"{self.brand} {self.model}: Starts silently. Battery capacity: {self.battery_capacity} kWh."


# Polymorphic function
def start_any_vehicle(vehicle):
    # Will call the correct start_engine() based on object's class
    print(vehicle.start_engine())


# -------------------- Example Usage --------------------

# Vehicle instance
v = Vehicle("Generic", "ModelX")
start_any_vehicle(v)
print(v.stop_engine())

print()

# Car instance
c = Car("Toyota", "Corolla", 4)
start_any_vehicle(c)
print(c.open_trunk())

print()

# ElectricCar instance (multiple inheritance in action)
ec = ElectricCar("Tesla", "Model S", 4, 100)
start_any_vehicle(ec)
print(ec.charge())
print(ec.open_trunk())

