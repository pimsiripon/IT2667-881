class Item:
    
    def __init__(self,name:str,price:float,quantity = 1) -> None:
        assert price > 0,f"price {price} must greater than 0"
        assert quantity > 0,f"quantity {quantity} must greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
       return self.price * self.quantity
    
    def __del__(self):
        print("Oblect was destroyed")

if __name__ == "__main__":
    item1 = Item("Monitor",5600)
    item2 = Item("Mouse",1500,2)
    print("===Totol Price ==")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")
    
  