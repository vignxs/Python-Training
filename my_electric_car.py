from car import Battery, Car


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()
