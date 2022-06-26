class Measure:
    def __init__(self) -> None:
        self.resulf = 0
    
    def inch_cm(self,number:float):
       self.resulf = number * 2.54
       return self.resulf

    def cm_inch(self,number:float):
        self.resulf = number / 2.54
        return self.resulf