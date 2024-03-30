import tkinter
window=tkinter.Tk()
window.title("bmi")
window.minsize(width=600, height=600)



def calculate():
    kilo = (kiloentry.get())
    boy= (boyentry.get())
    bmi = float(kilo) / (((float(boy)/100)**2))
    if bmi <18:
            mynewlabel= tkinter.Label(window,text="Zayıfsın")
            mynewlabel.pack()
    elif bmi>18.5 and bmi<25:
             mynewestlabel=tkinter.Label(window,text="Normalsin")
             mynewestlabel.pack()
    elif bmi>25 and bmi<30:
             mylyl=tkinter.Label(window,text="kilolusun")
             mylyl.pack()
    elif bmi>30:
             myll=tkinter.Label(window,text="Obez")
             myll.pack()
    print(bmi)


mylabel=tkinter.Label(window,text="Kilonuzu girin")
mylabel.pack()
kiloentry=tkinter.Entry()
kiloentry.pack()
mylabel2=tkinter.Label(window,text="Boyunuzu girin")
mylabel2.pack()
boyentry=tkinter.Entry()
boyentry.pack()
mybutton=tkinter.Button(window,text="Hesapla", command=calculate)
mybutton.pack()

window.mainloop()