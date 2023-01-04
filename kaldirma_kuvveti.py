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

