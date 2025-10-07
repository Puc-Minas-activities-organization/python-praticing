class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print("you are driving")
    
    def stop(self):
        print("you are not driving")
    
    def describe(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")