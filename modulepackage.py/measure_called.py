# วิธี่ที่ 1
from pickletools import float8
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    # ให้useเลือกแปลงค่า inch ,cm
    choice = input(f'Choose menu (1: inch,2: cm): ')
    # รับค่าจากuse
    number = float(input("Please enter an integer: "))
    
    if choice == '1':
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.cm_inch(number):.2f} cm')
    else:
        print('Choose wrong menu')

