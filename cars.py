class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def __str__(self):
        return f"{self.horsepower} HP {self.engine_type} engine"


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Engine: {self.engine}")


audi_engine = Engine(250, "Petrol")
bmw_engine = Engine(300, "Diesel")
mercedes_engine = Engine(350, "Hybrid")

audi_car = Car("Audi", audi_engine)
bmw_car = Car("BMW", bmw_engine)
mercedes_car = Car("Mercedes", mercedes_engine)

audi_car.display_info()
print()
bmw_car.display_info()
print()
mercedes_car.display_info()
