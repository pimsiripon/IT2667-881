class Car:
    brand = "Toyota"

    def __init__(self,model:str,colour:str,year:int,price:int) :
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    #instancemethod
    def printCarDetail(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:,.2f}")

    #staticmethod ไม่มีคำว่า self
    @staticmethod
    def get_static_method():
        text = "static"
        print(f"In {text} method")
        #ตัวแปล text ไม่สามารถเรียกใช้ใน printCarDetail()ได้
        #ตัวแปล text .ใช้ได้เฉพาะget_static_method() เท่านั้น

    #class method ต้องมีคำว่า cls
    @classmethod
    def __del__(self):
        my_text = "Class"
        print(f"This is {my_text} method")


    def __del__(self):
        print("Oblect was destroyed")

if __name__ == "__main__":
    my_car = Car("Cross","white",2022,1500000)
    my_car.printCarDetail() 

    #เรียกใช้ static method
    Car.get_static_method()
    my_car.get_static_method()

   