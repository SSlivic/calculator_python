from tkinter import *
from tkinter import messagebox
import math

root=Tk()
e=Entry(root,font="Ariel 24")
e.grid(row=0, column=0,columnspan=4,padx=10,pady=10)
#e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


global operacija, f_num, geometrija,memory, mmr
global new_entry
new_entry = False  # Začetna vrednost je False




def btn_CE():

    e.delete(0, END)

def btn_C():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)

def btn_plus():
    first_number=e.get()
    e.delete(0, END)
    global operacija
    operacija="+"
    global f_num
    f_num=float(first_number)


def btn_deljenje():
    first_number=e.get()
    global operacija, f_num
    operacija="/"
    f_num=float(first_number)

    e.delete(0,END)


def btn_oduzimanje():
    first_number = e.get()
    global operacija, f_num
    f_num = float(first_number)
    operacija="-"
    e.delete(0, END)

def btn_mnozenje():
    first_number = e.get()
    global operacija, f_num
    f_num = float(first_number)
    operacija = "*"
    e.delete(0,END)

def sqrt():
    global operacija, f_num
    first_number = e.get()
    f_num = float(first_number)
    operacija = "sqrt"
    e.delete(0, END)

def sinus():
    first_number = e.get()
    global geometrija, f_num
    f_num = float(first_number)
    geometrija = "sin"
    e.delete(0, END)
    e.insert(0, math.sin(f_num))
def cosinus():
    first_number = e.get()
    global geometrija, f_num
    f_num = float(first_number)
    geometrija = "cos"
    e.delete(0, END)
    e.insert(0, math.cos(f_num))
def tg():
    first_number = e.get()
    global geometrija, f_num
    f_num = float(first_number)
    geometrija = "tg"
    e.delete(0, END)
    e.insert(0, math.tan(f_num))


# Globalna varijabla za memoriju
memory = 0
mmr = None

def btn_mPlus():
    global memory,mmr,new_entry
    mmr='m+'
    try:
        memory += float(e.get())  # Dodavanje trenutne vrednosti u memoriju
        e.delete(0, END)
        new_entry = True
    except ValueError:
        messagebox.showerror("showerror", "Invalid input")  # Obrada greške

def btn_mMinus():
    global memory,mmr,new_entry
    mmr='m-'
    try:
        memory -= float(e.get())  # Oduzimanje trenutne vrednosti od memorije
        e.delete(0, END)
        new_entry = True
    except ValueError:
        messagebox.showerror("showerror", "Invalid input")



def btn_mc():
    global memory,mmr,new_entry
    mmr='mc'
    memory = 0  # Resetovanje memorije
    e.delete(0, END)
    new_entry = True




def btn_mr():
    global memory,mmr,new_entry
    mmr='mr'
    e.delete(0, END)
    e.insert(0, memory)
    new_entry = True





def btn_click(number):
    global new_entry
    if new_entry:  # Če je rezultat prikazan, počisti polje
        e.delete(0, END)
        new_entry = False
    trenutni_vnos = e.get()
    if number == "." and "." in trenutni_vnos:
        return
    e.delete(0, END)
    e.insert(0, str(trenutni_vnos) + str(number))


def equal():
    global operacija, new_entry

    try:
        second_number=e.get()
        e.delete(0, END)

        rezultat = None

        if (operacija =="+"):
            rezultat=f_num+float(second_number)

           # e.insert(0,f_num+float(second_number))
        elif (operacija =="-"):
            rezultat=f_num-float(second_number)


           # e.insert(0, f_num-float(second_number))
        elif (operacija =="*"):
            rezultat = f_num * float(second_number)

           # e.insert(0, f_num * (float(second_number)))

        elif (operacija == "/"):

            if float(second_number)==0:
                messagebox.showerror("showerror", "Error")
                return
            rezultat = f_num / float(second_number)
            #e.insert(0,rezultat)
           # e.insert(0,f_num /(float(second_number)))


        elif (operacija =="sqrt"):
            e.insert(0, math.sqrt(f_num))

        elif ((mmr=="mr") or (mmr=="m-") or (mmr=="m+") or (mmr=="mc")):
            e.insert(0, memory)


        if rezultat is not None:
          e.delete(0, END)
          if rezultat.is_integer():  # Funkcija preveri, ali je število celo
            e.insert(0, int(rezultat))


          else:
            e.insert(0, rezultat)  # Prikaz za decimalna števila
            new_entry = True  # Nastavi, da začne nov vnos od začetka
    except ValueError:
       messagebox.showerror("showerror", "Invalid input")
  #  except ValueError:
     #   messagebox.showerror("showerror", "Invalid input")



BtnJednako=Button(root,text="=",font=("Ariel 20"), bg="green", command=equal, padx=20, pady=7)
BtnJednako.grid(row=0,column=4)

Btn1=Button(root,text="1", command=lambda:btn_click(1), padx=35, pady=20)
Btn1.grid(row=1 ,column=0)


Btn2=Button(root,text="2",command=lambda:btn_click(2),  padx=35, pady=20)
Btn2.grid(row=1,column=1)


Btn3=Button(root,text="3", command=lambda:btn_click(3), padx=35, pady=20)
Btn3.grid(row=1 ,column=2)

Btn4=Button(root,text="4", command=lambda:btn_click(4),  padx=35, pady=20)
Btn4.grid(row=2 ,column=0)

Btn5=Button(root,text="5", command=lambda:btn_click(5),  padx=35, pady=20)
Btn5.grid(row=2 ,column=1)

Btn6=Button(root,text="6", command=lambda:btn_click(6), padx=35, pady=20)
Btn6.grid(row=2 ,column=2)

Btn7=Button(root,text="7", command=lambda:btn_click(7), padx=35, pady=20)
Btn7.grid(row=3 ,column=0)

Btn8=Button(root,text="8", command=lambda:btn_click(8),  padx=35, pady=20)
Btn8.grid(row=3 ,column=1)

Btn9=Button(root,text="9", command=lambda:btn_click(9), padx=35, pady=20)
Btn9.grid(row=3 ,column=2)

Btn0=Button(root,text="0", command=lambda:btn_click(0),  padx=35, pady=20)
Btn0.grid(row=4 ,column=1)

BtnPika=Button(root,text=".", command=lambda:btn_click("."),  padx=35, pady=20)
BtnPika.grid(row=4 ,column=2)

BtnC=Button(root,text="C", command=lambda:btn_C(),  padx=35, pady=20)
BtnC.grid(row=4 ,column=0)

BtnCE=Button(root,text="CE", command=lambda:btn_CE(), padx=35, pady=20, bg="red")
BtnCE.grid(row=5 ,column=4)

BtnPlus=Button(root,text="+", command=lambda:btn_plus(),  padx=35, pady=20)
BtnPlus.grid(row=1 ,column=3)
BtnMinus=Button(root,text="-",command=lambda:btn_oduzimanje(),  padx=35, pady=20)
BtnMinus.grid(row=2,column=3)
BtnPuta=Button(root,text="*" ,command=lambda:btn_mnozenje(), padx=35, pady=20)
BtnPuta.grid(row=3 ,column=3)
BtnDeljeno=Button(root,text="/", command=lambda:btn_deljenje(), padx=35, pady=20)
BtnDeljeno.grid(row=4 ,column=3)


BtnMC=Button(root,text="MC", command=lambda:btn_mc(), padx=35, pady=20)
BtnMC.grid(row=5 ,column=3)
BtnMplus=Button(root,text="M+", command=lambda:btn_mPlus(), padx=35, pady=20)
BtnMplus.grid(row=5 ,column=0)
BtnMminus=Button(root,text="M-", command=lambda:btn_mMinus(), padx=35, pady=20)
BtnMminus.grid(row=5,column=1)
BtnMR=Button(root,text="MR" ,command=lambda:btn_mr(), padx=35, pady=20)
BtnMR.grid(row=5 ,column=2)



Btnsin=Button(root,text="sin", command=sinus, padx=35, pady=20)
Btnsin.grid(row=1 ,column=4)
Btncos=Button(root,text="cos", command=cosinus,padx=35, pady=20)
Btncos.grid(row=2,column=4)
Btntg=Button(root,text="tg" ,command=tg, padx=35, pady=20)
Btntg.grid(row=3 ,column=4)

BtnSqrt=Button(root,text="sqrt", command=sqrt, padx=35, pady=20)
BtnSqrt.grid(row=4,column=4)

root.mainloop()
