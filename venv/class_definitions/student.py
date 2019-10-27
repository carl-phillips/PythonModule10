
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        try:
            self.last_name = lname
        except ValueError:
            print("ERROR")
        try:
            self.first_name = fname
        except ValueError:
            print("ERROR")
        try:
            self.major = major
        except ValueError:
            print("ERROR")
        try:
            self.gpa = gpa
        except ValueError:
            print("ERROR")

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


if __name__ == '__main__':
    s = Student("Phillips", 'Carl', "CIS", 3.78)
    print(s.__str__())