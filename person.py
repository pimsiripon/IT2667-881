from email.errors import MalformedHeaderDefect
from ntpath import join


class Person:
    def __init__(self,name,gender,profession) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self):
        self.study = hours

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')

#person1
jessa = Person('Jessa','Female','Solfware Engineer')
jessa.work()
jessa.show()

#person2
jon = Person('Jon','Male','Docter')
jon.study = 15
jon.work()
jon.show()

#person3
Lisa = Person('Lisa','Female','Singer')
Lisa.study = 10
Lisa.work()
Lisa.show()
