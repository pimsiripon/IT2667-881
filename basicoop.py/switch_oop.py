class Switch():
    def __init__(self) -> None:
        self.switch_status = False
        
    def turnon(salf):
        salf.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show_status(self):
        if (self.switch_status):
            print(f"ไฟเปิด")
        else:
            print(f"ไฟปิด")

#สร้างวัตถุobject
sobj = Switch()

if __name__ == "__main__":
    sobj.show_status()
    sobj.turnon()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()