class Area:
    def __init__(self) -> None:
        self.__base = 0
        self.__high = 0
    
    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,value):
        self.__base = value

# getter ของhigh
    @property
    def high(self):
        return self.__high
# serter ของhigh
    @base.setter
    def high(self,value):
        self.__high = value

    def compute_area(self):
        return 0.5 * self.base * self.high
        

    
