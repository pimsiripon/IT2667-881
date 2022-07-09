from multiprocessing.sharedctypes import Value
from vehicleabstract import Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__year = 0
        self.__maintanance = 0

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self,value):
        self.__year  = value

    @property
    return self.__maintanance


    @maintanance.setter
    def maintanance(self,value):
        self.__maintanance  = value

    def show_detail(self):
        super().show_detail()
        print('==== Car Detail ====')
        print(f'{self.brand} with speed {self.speed}/km/hr')
        print(f'manufactered in {self.year}')
# 
    def show_maintanance(self):
        print(f'The las')

class Truck(Vehicle):
    def __init__(self, brand, speed) -> None:
        super().__init__(brand, speed)
        self.__capacity = 1000
        set.__wheels = 4

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self,value):
        self.__capacity  = value

    @property
    def wheels(self):
        return self.wheels

    @wheels.setter
    def wheels(self,value):
        self.__wheels  = value

    def show_detail(self):
        super().show_detail()
        print("++++ Truck Detail++++")
        print(f'{self.brand}whit speed {self.speed} km/hr')
        print(f'carry {self.capacity} tons')

    def show_price(self):
        if self.wheels == 4:
            print = 1000
            self.wheela == 6:
            print = 


class Motocycle(Vehicle):
