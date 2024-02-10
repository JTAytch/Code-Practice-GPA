class Student:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.grade_point = 0
    self.credits = 0
    self.gpa = 0

  def calculate_gpa(self):
    if self.credits > 0:
      self.gpa = self.grade_point / self.credits
    else:
      self.gpa = 0

  def get_gpa(self):
    return self.gpa

def main():
  first_name = input("Enter student's first name: ")
  last_name = input("Enter student's last name: ")
  student = Student(first_name, last_name)

  while True:
    try:
        credits = float(input("Enter course credits (or '0' to quit): "))
        if credits == 0:
            break
        grade = input("Enter course grade (A, B+, B, C+, C, D, or F): ").upper()
        if grade not in ["A", "B", "B+", "C", "C+", "D", "F"]:
            raise ValueError("Invalid grade entered.")
  
        grade_points = {
            "A": 4,
            "B": 3,
            "B+": 3.5,
            "C": 2,
            "C+": 2.5,
            "D": 1,
            "F": 0
        }[grade]
  
        student.grade_point += grade_points * credits
        student.credits += credits
  
    except ValueError:
        print("Invalid input. Please enter a valid number for credits and a valid grade (A, B,           B+, C, C+, D, or F).")
  
  student.calculate_gpa()
  
  print(f"{student.first_name} {student.last_name}'s cumulative GPA: {student.get_gpa():.2f}")

if __name__ == "__main__":
  main()