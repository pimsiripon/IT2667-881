class Person:
    def __init__(self,name:str,gender:str,profession:str,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')
    
    def __del__(salf):
        print("Object was destroyed")

if __name__ =="__main__":
    #person1
    jessa = Person('Jessa','Female','Solfware Engineer',0)
    jessa.work()
    jessa.show()

    #person2
    jon = Person('Jon','Male','Docter',15)
    jon.work()
    jon.show()

    #person3
    Lisa = Person('Lisa','Female','Singer',10)
    Lisa.work()
    Lisa.show()
