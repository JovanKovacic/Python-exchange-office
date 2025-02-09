from tkinter import *

def konvertuj(*args):
    ulaznaValuta = meniInput.get()
    izlaznaValuta = meniOutput.get()
    iznos = unos.get()

    if ulaznaValuta == "Valuta" or izlaznaValuta == "Valuta":
        izlaz.config(text="Izaberite valutu")
        return

    try:
        iznos = float(iznos)
    except ValueError:
        izlaz.config(text="Nevalidan unos")
        return

    kursevi = {
        "EURO": {"USD": 1.04, "RSD": 117.09, "EURO": 1},
        "USD": {"EURO": 0.96, "RSD": 112.38, "USD": 1},
        "RSD": {"EURO": 0.0085, "USD": 0.0089, "RSD": 1},
    }

    if ulaznaValuta not in kursevi or izlaznaValuta not in kursevi[ulaznaValuta]:
        izlaz.config(text="Nevalidna valuta")
        return

    kurs = kursevi[ulaznaValuta][izlaznaValuta]
    konv = iznos * kurs
    izlaz.config(text=f"{konv:.2f}")

#Podešavanje prozora
width = 500
height = 600

window = Tk()
window.title("Menjacnica")
window.geometry("500x600")

icon = PhotoImage(file='D:\Programiranje\PythonProjekti\Menjacnica\dolar.png')
window.iconphoto(True, icon)

window.config(background="#333131")
window.resizable(False, False)

#Naslov
naslov = Label(window, text="Menjacnica", font=('arial', 40, 'bold'), fg='darkorchid3', bg="#333131", bd=10)
naslov.pack()

#Border unosa
b1 = Frame(window, background="darkorchid3", bd=2)

unos = StringVar()
unos.trace_add("write", konvertuj)

#Unos
ulaz = Entry(b1, bd=0, textvariable=unos, font=("arial", 20), fg="darkorchid3", bg="#333131", width=10)
ulaz.pack()
b1.pack()

#⇄
znak = Label(window, text="⇄", font=('arial', 40), fg='darkorchid3', bg="#333131")
znak.pack()

#Border ispisa
b2 = Frame(window, background="darkorchid3", bd=2)

#Ispis
izlaz = Label(b2, font=("arial", 20), fg="darkorchid3", text="0.00", width=10, background="#333131")
izlaz.pack(padx=1, pady=1)
b2.pack()

#Ulaz
options = ["EURO", "USD", "RSD"]
meniInput = StringVar()
meniInput.set("Valuta")
dropInput = OptionMenu(window, meniInput, *options)
dropInput.place(x=80, y=85)

#Izlaz
meniOutput = StringVar()
meniOutput.set("Valuta")
dropOutput = OptionMenu(window, meniOutput, *options)
dropOutput.place(x=350, y=200)


window.mainloop()
