class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phon = ''

    def new_customer(self):
        self.name = input('Enter name : ')
        self.address = input('Enter address : ')
        self.phon =input('Enter phon :')

    def cus_info(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhon: {self.phon}'