class Student:
    def __init__(self,id:str,name:str,major="IT") -> None:
       self.id = id
       self.name = name
       self.major = major

    def displayDetail(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        
    def __del__(self):
        print("Oblect was destroyed")

if __name__ == "__main__":
    jessica = Student("111","Jassica","IT")
    jessica.displayDetail()

    john = Student("112","John","MKT")
    john.displayDetail()

    james = Student("113","James")
    james.displayDetail()