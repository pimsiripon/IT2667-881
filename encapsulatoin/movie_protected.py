class Movie:
    def __init__(self,) -> None:
        
        self._title = None
        self._year = None
        self._genre = None

    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self._year = year
        self._genre = genre

    def _getmovie_detail(self):
        print(f'Titly: {self._title}')
        print(f'Year: {self._year}')
        print(f'Genre: {self._genre}')

# คลาส movie,documentaryอยู่ในไฟล์เดียวกัน ไม่่ต้อง import
class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)

    def add_channel(self,ch:str):
        self.channel = ch

    def _getmovie_detail(self):
        Movie._getmovie_detail(self)
        print(f'Channel: {self.channel}')

# สร้าว object
if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie(f'My Octopus Teacher',2022,'Documentary')
    m1.add_channel('NetFlix')
    m1._getmovie_detail()

