from currency_converter import CurrencyConverter
import tkinter as tk
c = CurrencyConverter()
#print (c.convert(12,"USD","INR"))

window = tk.Tk()

window.geometry("500x350")
window.title("Currency Converter")

def clicked():
    amount = entry1.get()
    try:
        amount = float(amount)  
    except ValueError:
        print("Please enter a valid number.")
        return
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window, text =data,font = "Times 16").place(x=200, y=300)


label = tk.Label(window, text="Currency Converter", font = "Times 20").place(x=120,y=40)
label1 = tk.Label(window, text="Enter Amount:", font = "Times 16").place(x=70,y=100)
entry1 = tk.Entry(window)

label2 = tk.Label(window, text="Enter Current Currency:", font = "Times 16").place(x=70,y=140)
entry2 = tk.Entry(window)

label3 = tk.Label(window, text="Enter Desired Currency:", font = "Times 16").place(x=70,y=180)
entry3 = tk.Entry(window)

button = tk.Button(window,text = "click", font = "Times 16", command=clicked).place(x=220,y=250 )



entry1.place(x=275, y=105)
entry2.place(x=275, y=145)
entry3.place(x=275, y=185)

window.mainloop()
