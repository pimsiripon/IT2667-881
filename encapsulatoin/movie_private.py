class Movie:
    def __init__(self,) -> None:
        
        self.__title = None
        self.__year = None
        self.__genre = None
        self.__rating = 5

    def _add_movie(self,title:str,year:int,genre:str,rating=5):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__rating = rating


    def __getmovie_detail(self):
        print(f'Titly: {self.__title}')
        print(f'Year: {self.__year}')
        print(f'Genre: {self.__genre}')
        print(f'Reying: {self.__rating}')

    def print_detail(self):
        self.__getmovie_detail()

    class Documentary(Movie):
        def __init__(self) -> None:
            Movie.__init__(self)

        def add_channel(self,ch:str):
        self.channel = ch

        def print_drtail(self):
            super().print_detail()
            print(f'Channel: {self.channel}')

if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie(f'My Octopus Teacher',2022,'Documentary')
    m1.add_channel('NetFlix')
    m1._Movie__getmovie_detail()
    m1.print_detail()