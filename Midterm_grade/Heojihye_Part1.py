import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("400x200")


label_c = ttk.Label(root, text = "Enter Celsius :")
label_c.grid(row = 0, column =0)

entry_c = ttk.Entry(root)
entry_c.grid(row = 0, column = 1, pady = 5, padx = 5)

label_result = ttk.Label(root, )
label_result.grid(row =2, column = 0, pady = 10)


def cal_Fahrenheit(c):
    c = float(c)
    f = c*(9/5) + 32
    return f


def ctof():
    c = entry_c.get()
    result = cal_Fahrenheit(c)
    label_result.config(text = f"Result : {result} 'F")
    

button_c = ttk.Button(root, text = "Convert", command = ctof)
button_c.grid(row = 1, column = 0, pady =10)

root.mainloop()

