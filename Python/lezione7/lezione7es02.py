class Student:

    def __init__(self, name: str, study_program: str):
        self.name: str = name
        self.study_program: str = study_program

    def __str__(self):
        return f'Student(name{self.name}, study_program={self.study_program}, age={self.age},
        gende={self.gender})'
    
    def set_age(self, new_age: int):
        self.age = new_age
    def set_gender(self, new_gender: str):
        self.gender = new_gender
    
lorenzo = Student("lorenzo", "fullstack")
print(lorenzo)
