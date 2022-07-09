from multiprocessing.sharedctypes import Value


class Shape:
    def __init__(self) -> None:
        self.__shape = None
        self.__area = 0

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self,value):
        self.shape = value


    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self,value):
        self.area = value  

    def compute_area(self):
        pass  
