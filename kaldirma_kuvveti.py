from tkinter import *
from tkinter import messagebox

def kk_hesapla():
    v_batan = int(v_batan_tf.get())
    d_sivi = int(d_sivi_tf.get())
    g = int(yercekimi_input.get())
    kaldirma_kuvveti = (v_batan*d_sivi*g)
    kaldirma_kuvveti = round(kaldirma_kuvveti, 1)

    messagebox.showinfo('Hesaplanan Kaldirma Kuvveti', f'Hesaplanan Kaldirma Kuvveti = {kaldirma_kuvveti}')
    

ws = Tk()
ws.title('Kaldirma Kuvveti Hesaplama')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10
    pady=10
)
frame.pack(expand=True)


v_batan_label = Label(
    frame,
    text="V(batan):"
)
v_batan_label.grid(row=1, column=1)

d_sivi_label=Label(
    frame,
    text="d(sivi) :"
)
d_sivi_label.grid(row=3, column=1)

yercekimi_label = Label(
    frame,
    text="g : ",

)
yercekimi_label.grid(row=4, column=1)


yercekimi_input = Entry(
    frame,
)
yercekimi_input.grid(row=1, column=2, pady=5)

d_sivi_tf = Entry(
    frame,
)
d_sivi_tf.grid(row=3, column=2, pady=5)

v_batan_tf = Entry(
    frame,
)
v_batan_tf.grid(row=4, column=2, pady=5)



frame3 = Frame(
    frame
)
frame3.grid(row=5, columsnpan=3, pady=10)

hesapla_btn = Button(
    frame3,
    text='Hesapla',
    command=kk_hesapla
)
hesapla_btn.pack(side=LEFT)
