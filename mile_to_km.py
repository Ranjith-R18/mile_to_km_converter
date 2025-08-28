from tkinter import *

window = Tk()
window.geometry("300x100")
window.title("Mile to KM converter")

def convert():
    mil = float(miles.get())
    kilometer= mil*1.609
    result.config(text=f"{kilometer}")

miles=Entry(width=8)
miles.grid(row=0,column=1)

label=Label(text="Miles")
label.grid(row=0,column=2)

result=Label(text="0")
result.grid(row=1,column=1)

km=Label(text="KM")
km.grid(row=1,column=2)

button=Button(text="calculate",command=convert)
button.grid(row=2,column=1)

window.mainloop()