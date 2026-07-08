import tkinter as tk

def hlavni_okno():
    okno = tk.Tk()
    okno.title("Moje aplikace")
    okno.geometry("300x200")

    label = tk.Label(okno, text="Zadej jméno:")
    label.pack()

    vstup = tk.Entry(okno)
    vstup.pack()

    button = tk.Button(okno, text="Potvrď")
    button.pack()

    okno.mainloop()

if __name__ == "__main__":
    hlavni_okno()