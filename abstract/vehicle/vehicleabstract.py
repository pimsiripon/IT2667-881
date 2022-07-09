from abc import ABC, abstractclassmethod

class Vehicle,(ABC):
    def __init__(self,brand,speed) -> None:
        super().__init__()
        self.brand = brand
        self.speed =speed
        self.gear = 0 
        self.seat = 0
    @abstractclassmethod
    def show_detail(self):
        