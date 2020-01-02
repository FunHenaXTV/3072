import tkinter as tk
from random import randint
from tkinter import messagebox as mb



class Desk:
    def __init__(self):
        self.objects = []
        self.texts = []
        self.points = []
        k = 0

        empty_list = [0, 0, 0, 0]
        self.objects = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.texts = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        i = 0
        j = 0
        for y in range(2, 502, 125):
            for x in range(2, 502, 125):
                self.points = [x, y, x, y+125, x+125, y+125, x+125, y]
                self.objects[i][j] = (canvas.create_polygon(self.points, outline="#bbb09e", fill="#bbb09e"))
                self.texts[i][j] = (canvas.create_text(62.5+x, 62.5+y, text=str(i)+str(j), font=30))
                i += 1
            j += 1
            i = 0
        x1 = randint(0, 3)
        x12 = randint(0, 3)
        y1 = randint(0, 3)
        y12 = randint(0, 3)
        while x1 == y1 and y12 == x12:
            x1 = randint(0, 15)

        x2 = randint(1, 3)
        y2 = randint(1, 3)
        if x2 == 1 or x2 == 2:
            canvas.itemconfig(self.texts[x1][x12], text='3')
        else:
            canvas.itemconfig(self.texts[x1][x12], text='6')

        if y2 == 1 or y2 == 2:
            canvas.itemconfig(self.texts[y1][y12], text='3')
        else:
            canvas.itemconfig(self.texts[y1][y12], text='6')
 
        self.check_color(x1, x12)
        self.check_color(y1, y12)


    def check_event(self, event):
        e = event.keysym
        if e == "Up":
            self.Up()
        if e == "Down":
            self.Down()
        if e == 'Right':
            self.Right()
        if e == 'Left':
            self.Left()

    def Up(self):
        for i in range(4, 16):
            if canvas.itemcget(self.texts[i], 'text') != '':
                pass

    def Down(self):
        pass

    def Right(self):
        pass

    def Left(self):
        pass


    def check_color(self, i, j):
        if canvas.itemcget(self.texts[i][j], 'text') == '3':
            canvas.itemconfig(self.objects[i][j], fill='#eee4da', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '6':
            canvas.itemconfig(self.objects[i][j], fill='#eedfc8', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '':
            canvas.itemconfig(self.objects[i][j], fill='#bbb09e', outline="#bbb09e")
        elif canvas.itemcget(self.texts[i][j], 'text') == '12':
            canvas.itemconfig(self.objects[i][j], fill='#f3b079', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '24':
            canvas.itemconfig(self.objects[i][j], fill='#f59563', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '48':
            canvas.itemconfig(self.objects[i][j], fill='#f97c60', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '96':
            canvas.itemconfig(self.objects[i][j], fill='#f85e3a', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '192':
            canvas.itemconfig(self.objects[i][j], fill='#edce73', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '384':
            canvas.itemconfig(self.objects[i][j], fill='#edcb60', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '768':
            canvas.itemconfig(self.objects[i][j], fill='#eec750', outline="#fff")            
        elif canvas.itemcget(self.texts[i][j], 'text') == '1536':
            canvas.itemconfig(self.objects[i][j], fill='#ecc441', outline="#fff")
        elif canvas.itemcget(self.texts[i][j], 'text') == '3072':
            canvas.itemconfig(self.objects[i][j], fill='#edc12c', outline="#fff")
        else:
            canvas.itemconfig(self.objects[i][j], fill='#fc3f3d')



root = tk.Tk()
root.title("3072")
root.configure(bg='#bbb09e', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=504, height=504, highlightthickness=0)
canvas.pack()


desk = Desk()

score = 0


root.bind_all('<Key>', desk.check_event)




root.mainloop()
