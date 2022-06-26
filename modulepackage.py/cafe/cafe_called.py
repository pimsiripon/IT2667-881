# วิธีที่ 1
from cafe_module import Desserts
from cafe_module import Drinks

# วิธีที่ 2

desserts = Desserts()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drinks('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drinks('น้ำผลไม้')
print(drinks.show_drinks())