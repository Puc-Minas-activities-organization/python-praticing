class Employee:
    def __init__(self, name, position):
        self.name = name
        if Employee.is_valid_position(position):
            self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cooker", "Janitor"]
        return position in valid_positions
