import tkinter as tk
from random import randint
from tkinter import messagebox as mb



class Desk:
	def __init__(self):
		pass


	def check_event(self):
		pass




root = tk.Tk()
root.title("3072")
root.configure(bg='#bbb09e', width=600, height=600)

canvas = tk.Canvas(root, bg='#fff', width=504, height=504, highlightthickness=0)
canvas.pack()


desk = Desk()

score = 0


root.bind_all('<Key>', desk.check_event)




root.mainloop()