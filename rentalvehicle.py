class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, duration):
        return self.rental_rate * duration

class Car(Vehicle):
    def __init__(self, model, rental_rate, insurance_fee):
        super().__init__(model, rental_rate)
        self.insurance_fee = insurance_fee

    def calculate_rental(self, duration):
        return (self.rental_rate * duration) + self.insurance_fee

class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee

    def calculate_rental(self, duration):
        return (self.rental_rate * duration) + self.helmet_fee

class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_fee_per_ton, tons):
        super().__init__(model, rental_rate)
        self.load_fee_per_ton = load_fee_per_ton
        self.tons = tons

    def calculate_rental(self, duration):
        return (self.rental_rate * duration) + (self.load_fee_per_ton * self.tons)

# Example usage
vehicles = [
    Car("Hatchback", 40, 15),
    Bike("Himalayan", 10, 5),
    Truck("truck", 100, 20, 5)
]

rental_duration = 4 # days

for v in vehicles:
    print(f"{v.model} rental cost for {rental_duration} days: ${v.calculate_rental(rental_duration):,.2f}")
