from tkinter import *
from PIL import Image, ImageTk
import os, sys, random


occupied = []
default_items = []
item_id = None
game_over = False


def on_enter(event):
    canvas.config(cursor="hand2")


def on_leave(event):
    canvas.config(cursor="")


def click(event):
    global item_id
    global game_over

    if game_over:
        return
    
    item_id = canvas.find_withtag(CURRENT)[0]
    if item_id in occupied:
        return
    canvas.itemconfig(item_id, image=x_tk)
    occupied.append(item_id)
    if item_id in default_items:
        default_items.remove(item_id)
    if vitoria_x():
        return
    circ()


vitc_l1, vitc_l2, vitc_l3 = [], [], []
vitc_c1, vitc_c2, vitc_c3 = [], [], []
vitc_d1, vitc_d2 = [], []

vitcs = [vitc_l1, vitc_l2, vitc_l3, vitc_c1, vitc_c2, vitc_c3, vitc_d1, vitc_d2]

def circ():
    if default_items == []:
        return
    item_id = random.choice(default_items)
    canvas.itemconfig(item_id, image=circle_tk)
    occupied.append(item_id)
    default_items.remove(item_id)
    global game_over
    x, y = canvas.coords(item_id)

    if x == 96:
        vitc_c1.append('c1')
    elif x == 220:
        vitc_c2.append('c2')
    elif x == 344:
        vitc_c3.append('c3')

    if y == 96:
        vitc_l1.append('l1')
    elif y == 220:
        vitc_l2.append('l2')
    elif y == 344:
        vitc_l3.append('l3')

    if x == y:
        vitc_d1.append('d1')
    if (x,y) in [(96,344),(220,220),(344,96)]:
        vitc_d2.append('d2')

    for vc in vitcs:
        if len(vc) == 3:
            vit_label.config(text='PERDEU!', fg='#FF0000')
            game_over = True
    if not game_over:
        empate()


vitx_l1, vitx_l2, vitx_l3 = [],[],[]
vitx_c1, vitx_c2, vitx_c3 = [],[],[]
vitx_d1, vitx_d2 = [],[]

vitxs = [vitx_l1, vitx_l2, vitx_l3, vitx_c1, vitx_c2, vitx_c3, vitx_d1, vitx_d2]

def vitoria_x():
    global game_over
    x, y = canvas.coords(item_id)

    if x == 96:
        vitx_c1.append('c1')
    elif x == 220:
        vitx_c2.append('c2')
    elif x == 344:
        vitx_c3.append('c3')

    if y == 96:
        vitx_l1.append('l1')
    elif y == 220:
        vitx_l2.append('l2')
    elif y == 344:
        vitx_l3.append('l3')

    if x == y:
        vitx_d1.append('d1')
    if (x,y) in [(96,344),(220,220),(344,96)]:
        vitx_d2.append('d2')

    for vx in vitxs:
        if len(vx) == 3:
            vit_label.config(text='VENCEU!',fg='#008000')
            game_over = True
            return True
    if not game_over:
        empate()


def empate():
    global game_over
    if len(occupied) >= 9:
        vit_label.config(text='EMPATOU!', fg='#8B8000')
        game_over = True

       
def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


vits = [vitx_l1, vitx_l2, vitx_l3, vitx_c1, vitx_c2, vitx_c3, vitx_d1, vitx_d2]

janela = Tk()
janela.geometry('450x500')
janela.resizable(False,False)

canvas = Canvas(janela, width=450, height=450, bg='black')
canvas.pack()


default = Image.open("imgs/default.png")
default_tk = ImageTk.PhotoImage(default)

circle = Image.open("imgs/circle.png")
circle_tk = ImageTk.PhotoImage(circle)

x = Image.open("imgs/x.png")
x_tk = ImageTk.PhotoImage(x)


pos = [(96,96), (220,96), (344,96), (96,220), (220,220), (344,220), (96,344), (220,344), (344,344)]

for p in pos:
    default_id = canvas.create_image(p, image=default_tk, tags="default")
    default_items.append(default_id)
    canvas.tag_bind(default_id, "<Enter>", on_enter)
    canvas.tag_bind(default_id, "<Leave>", on_leave)
    canvas.tag_bind(default_id, "<Button-1>", click)


canvas.create_line(160, 40, 160, 400, width=2, fill='white')
canvas.create_line(50, 150, 400, 150, width=2, fill='white')
canvas.create_line(290, 40, 290, 400, width=2, fill='white')
canvas.create_line(50, 290, 400, 290, width=2, fill='white')


menu = Frame(janela)
menu.pack(pady=10, anchor=E)

texto = ""
vit_label = Label(menu, text=texto, font=('Arial', 16))
vit_label.pack(side=LEFT, padx=10)

btn_restart = Button(menu, text='Reiniciar', command=restart)
btn_restart.pack(side=RIGHT, padx=10)

janela.mainloop()