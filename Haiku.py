#Haiku Generato
import random
import tkinter
from tkinter import *
root = Tk()
root.geometry('{}x{}'.format(170, 100))
top_line = ["The heart of a child", "Edward Scissor-Hands", "2 Kids, One Sandbox", "Check yo privilege", "doing the right thing", "Mad Hacky-Sack Skills", "Being on fire", "Same-Sex ice dancing", "The forbidden fruit", "A salty surprise", "Morgan Freeman's voice", "Parting the red sea"]
middle_line = ["Teaching a robot to love", "The worlds worst human being", "A dingo ate my baby", "A child beauty pageant", "The Make-A-Wish Foundation", "Michael Jackson", "The profoundly handicapped", "A middle aged man on roller skates", ]
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
