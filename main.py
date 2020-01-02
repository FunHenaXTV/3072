import tkinter as tk
from random import randint
from tkinter import messagebox as mb



class Desk:
    def __init__(self):
        self.objects = []
        self.texts = []
        self.points = []
        k = 0
        for y in range(2, 502, 125):
            for x in range(2, 502, 125):
                self.points = [x, y, x, y+125, x+125, y+125, x+125, y]
                self.objects.append(canvas.create_polygon(self.points, outline="#bbb09e", fill="#bbb09e"))
                self.texts.append(canvas.create_text(62.5+x, 62.5+y, text='', font=30))

        x1 = randint(0, 15)
        y1 = randint(0, 15)
        while x1 == y1:
            x1 = randint(0, 15)

        x2 = randint(1, 3)
        y2 = randint(1, 3)
        if x2 == 1 or x2 == 2:
            canvas.itemconfig(self.texts[x1], text='3')
        else:
            canvas.itemconfig(self.texts[x1], text='6')

        if y2 == 1 or y2 == 2:
            canvas.itemconfig(self.texts[y1], text='3')
        else:
            canvas.itemconfig(self.texts[y1], text='6')
 
        self.check_color(x1)
        self.check_color(y1)


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
        pass

    def Down(self):
        pass

    def Right(self):
        pass

    def Left(self):
        pass


    def check_color(self, i):
        if canvas.itemcget(self.texts[i], 'text') == '3':
            canvas.itemconfig(self.objects[i], fill='#eee4da', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '6':
            canvas.itemconfig(self.objects[i], fill='#eedfc8', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '':
            canvas.itemconfig(self.objects[i], fill='#bbb09e', outline="#bbb09e")
        elif canvas.itemcget(self.texts[i], 'text') == '12':
            canvas.itemconfig(self.objects[i], fill='#f3b079', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '24':
            canvas.itemconfig(self.objects[i], fill='#f59563', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '48':
            canvas.itemconfig(self.objects[i], fill='#f97c60', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '96':
            canvas.itemconfig(self.objects[i], fill='#f85e3a', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '192':
            canvas.itemconfig(self.objects[i], fill='#edce73', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '384':
            canvas.itemconfig(self.objects[i], fill='#edcb60', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '768':
            canvas.itemconfig(self.objects[i], fill='#eec750', outline="#fff")            
        elif canvas.itemcget(self.texts[i], 'text') == '1536':
            canvas.itemconfig(self.objects[i], fill='#ecc441', outline="#fff")
        elif canvas.itemcget(self.texts[i], 'text') == '3072':
            canvas.itemconfig(self.objects[i], fill='#edc12c', outline="#fff")
        else:
            canvas.itemconfig(self.objects[i], fill='#fc3f3d')



root = tk.Tk()
root.title("3072")
root.configure(bg='#bbb09e', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=504, height=504, highlightthickness=0)
canvas.pack()


desk = Desk()

score = 0


root.bind_all('<Key>', desk.check_event)




root.mainloop()
