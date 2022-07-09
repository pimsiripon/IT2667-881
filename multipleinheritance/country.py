from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation_density(self):
        return self .population / self.area

    def show_detail(self):
        # ชื่อประเทศ
        print(f'Country: {self.name}')

        # สภานที่ตั้ง
        print(self.getcordinate())

        print(f'Area: {self.area}')
        print(f'Population: {self.population} Milllion')
        print(f'Density: {self.getpopulation_density()}')

        print(f'TimeZone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperature(C): {self.celsius()}')
        print(f'Temperature(F): {self.getfahrenhait()}')
        print(f'Weather: {self.getweather()}')
        print(self)


