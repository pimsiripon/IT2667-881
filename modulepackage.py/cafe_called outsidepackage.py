# วิธีที่ 1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks

# วิธีที่ 2
import cafe import cafe_module

desserts = cafe_module.Drinks()
print(desserts.show_desserts())

drinks =cafe_module.Drinks()
print(drinks.show_drinks())
drinks.add_drinks('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drinks('น้ำผลไม้')
print(drinks.show_drinks())