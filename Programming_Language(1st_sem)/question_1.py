# Create a class Student with instance variables name, roll_number, and marks in five subjects. Add
# three instance methods in this class to calculate total, percentage, and division of the marks obtained
# by the students. Use this class to find total marks obtained, percentage, and division of five students.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # list of 5 subject marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.marks)

    def calculate_division(self):
        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "Distinction"
        elif percentage >= 60:
            return "First Division"
        elif percentage >= 45:
            return "Second Division"
        else:
            return "Fail"



students = [
    Student("Allan", 1, [78, 82, 69, 85, 80]),
    Student("Alan", 2, [55, 61, 58, 64, 60]),
    Student("Alen", 3, [40, 42, 38, 45, 41]),
    Student("Allen", 4, [88, 90, 84, 86, 89]),
    Student("Saud", 5, [65, 70, 72, 68, 66])
]


for s in students:
    total = s.calculate_total()
    percentage = s.calculate_percentage()
    division = s.calculate_division()

    print("Name:", s.name)
    print("Roll Number:", s.roll_number)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Division:", division)
    print("----------------------")