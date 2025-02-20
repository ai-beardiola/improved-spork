class MyCar:

    def __init__(self):
        self.fuel_level = 10

    def drive_car(self):
        print("Driving car")
    def stop_car(self):
        print("Stopping car")
    def gear_car(self):
        print("Gear change")
    def decrease_fuel(self):
        self.fuel_level -= 1
        print(f"Fuel level is {self.fuel_level}")


my_car = MyCar()

my_car.drive_car()
my_car.stop_car()
my_car.gear_car()
my_car.decrease_fuel()