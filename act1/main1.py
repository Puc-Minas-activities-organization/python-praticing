from car import Car
from student import Student

#car1 = Car("Mustang", "2025", "black", True)
#car1.describe()

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 32)

student1.describe()
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")