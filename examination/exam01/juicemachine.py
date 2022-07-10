class JuiceOder:
    menu_type = "Juice"
    total = 0

    def __init__(self,menu:str,size:str,num = 1) -> None:
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
    
        }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price += 0
        elif self.size == 'L':
            self.price += 5
        else:
            self.price
        
        JuiceOder.total = self.price * self.num
        
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f' {self.menu} ({self.size} * ${self.price}) => ${JuiceOder.total} baht' 

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    order1 = JuiceOder("wj","L")
    order2 = JuiceOder("oj","R")
    order3 = JuiceOder("pj","L")
    
    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())