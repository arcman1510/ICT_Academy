from ITS.group import Group
from ITS.people.student import Student
from abc import ABC, abstractmethod

class CourseAB(ABC):

    def _init__(self, name: str):
        self.name: str = name
        self.groups: list[Group] = []

    @abstractmethod
    def register_student(self, student: Student):
        pass

    def add_group(self, group: Group):
        if group and group not in self.groups:
            self.groups.append(group)

    

