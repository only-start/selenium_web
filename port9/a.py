class Father():
    def  car(self):
        print("这是你爸爸的车子")
    def  huose(self):
        print("这是你爸爸的房子")

class Mother():
    def gongsi(self):
        print("这是你麻麻的公司")

class Son(Father,Mother):
    def house(self):
        print("这是我自己装修的房子")
    def wife(self):
        self.house()
        self.car()
        self.gongsi()
s =Son()
s.house()
s.wife()


