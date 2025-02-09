from tkinter import *
import requests

def getKurs(ulaznaValuta, izlaznaValuta):
    url = BaseURL + ulaznaValuta
    try:
        kurs = requests.get(url)
        data = kurs.json()
        if data["result"] == "success":
            return data["conversion_rates"].get(izlaznaValuta)
        else:
            print("Greska1")
            return None
    except Exception as e:
        print("GRESKA2:", e)
        return None 

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

    kurs = getKurs(ulaznaValuta, izlaznaValuta)

    if kurs is None:
        izlaz.config(text="Greska3")
        return

    konv = iznos * kurs
    izlaz.config(text=f"{konv:.2f}")

APIKey = "3f666a89599f0aa6c8875912"
BaseURL = f"https://v6.exchangerate-api.com/v6/{APIKey}/latest/"

width = 500
height = 600

window = Tk()
window.title("Menjacnica")
window.geometry("500x600")

icon = PhotoImage(file='D:\Programiranje\PythonProjekti\Menjacnica\dolar.png')
window.iconphoto(True, icon)

window.config(background="#333131")
window.resizable(False, False)

# Naslov
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

# ⇄
znak = Label(window, text="⇄", font=('arial', 40), fg='darkorchid3', bg="#333131")
znak.pack()

#Border ispisa
b2 = Frame(window, background="darkorchid3", bd=2)

#Ispis
izlaz = Label(b2, font=("arial", 20), fg="darkorchid3", text="0.00", width=10, background="#333131")
izlaz.pack(padx=1, pady=1)
b2.pack()

#Ulaz
options = ["EUR", "USD", "RSD"]
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