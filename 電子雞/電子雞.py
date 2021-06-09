from easygui import buttonbox
import random,time
class 雞():
    def __init__(self,體重,飽足感,開心度,健康度):
        self.體重 = 體重
        self.飽足感 = 飽足感
        self.開心度 = 開心度
        self.健康度 = 健康度
    def 餵食(self):
        if self.飽足感 != 100:
            self.飽足感 = 100
            self.體重 += random.randint(1,2)
        if self.飽足感 == 100:
            pass
    def 遊玩(self):
        self.飽足感 -= random.randint(40,60)
        if self.開心度 != 100:
            self.開心度 += random.randint(1,2)
        if self.飽足感 <= 0:
            self.飽足感 =0
        if self.飽足感 == 0:    
            self.體重 -= random.randint(1,2)
        
        
    def 打掃(self):
        if i == "屎.gif":
            self.健康度 += random.randint(10,13)
        else:
            self.健康度 += random.randint(1,3)
    def 狀態(self):
        print("體重:",self.體重)
        print("飽足感:",self.飽足感)
        print("開心度:",self.開心度)
        print("健康度:",self.健康度)
        
ch = buttonbox("","電子雞",image = "egg.gif",choices = ["開始遊戲"])
while True:
    if ch:
        egg = buttonbox("                                    孵化中...","電子雞",choices = ["繼續"])
        if egg:
            雞 = 雞(0,50,50,50,50)
            ch1 = buttonbox("","電子雞",image = "小雞.gif",choices = ["餵食","遊玩","打掃","狀態"])
            while True: 
                行為 = random.choice(["上廁所",""])
                if 行為 == "上廁所":
                    i = "屎.gif"
                    雞.健康度 -= 10
                else:
                    i = "小雞.gif"
                ch1 = buttonbox("","電子雞",image = i,choices = ["餵食","遊玩","打掃","狀態"])
                if ch1:
                    if ch1 == "餵食":
                        雞.餵食()
                    if ch1 == "遊玩":
                        雞.遊玩()
                    if ch1 == "打掃":
                        雞.打掃()
                    if ch1 == "狀態":
                        雞.狀態()
                else:
                    break
            break    
        else:
            break   
    else:
        break   

