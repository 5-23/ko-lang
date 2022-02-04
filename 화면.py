from tkinter import *

class 화면(Tk):
    def __init__(self):
        self.win = Tk()
        self.TkSize = [100,100]
        self.win.geometry(f"{self.TkSize[0]}x{self.TkSize[1]}")
    

    def 크기(self , 넓이 , 높이):
        self.size = [넓이,높이]
        self.win.geometry(f"{self.TkSize[0]}x{self.TkSize[1]}")

    def 버튼(self , 이름 = None , 이벤트 = None , x = None , y = None , 넓이 = None , 높이 = None):
        self.x = x
        self.y = y

        self.width = 넓이
        self.height = 높이

        self.button = Button(self.win , overrelief="solid" ,  text = 이름 , command = 이벤트 , height=self.height , width = self.width)
        self.button.place(x = self.x , y = self.y)




    def 시작(self):
        self.win.mainloop()