#Haiku Generato
import random
import tkinter
from tkinter import *
root = Tk()
root.geometry('{}x{}'.format(170, 100))
top_line = ["The heart of a child", "Edward Scissor-Hands", "2 Kids, One Sandbox", "Check yo privilege", "doing the right thing", "Mad Hacky-Sack Skills"]
middle_line = ["Teaching a robot to love", "The worlds worst human being", "A dingo ate my baby", "A child beauty pageant", "The Make-A-Wish Foundation", "Michael Jackson"]
bottom_line = ["Teenage pregnancy", "Kids with ass cancer", "Apologizing", "Being Fabulous", "Public Ridicule"]
def generate():
    top_line_choice = str(random.choice(top_line))
    middle_line_choice = str(random.choice(middle_line))
    bottom_line_choice = str(random.choice(bottom_line))
    haiku = top_line_choice + '\n' + middle_line_choice + "\n" + bottom_line_choice
    global haiku
generate()
l1 = Label(root, text=haiku)
l1.grid(row=0, column=0)
print(haiku)
def change():
    generate()
    l1.config(text=haiku)
b1 = Button(root, text='Generate!', command=change)
b1.place(x=30, y=60)


mainloop()
