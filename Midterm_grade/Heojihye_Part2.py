import tkinter as tk
from tkinter import ttk
import time
import threading

root = tk.Tk()
root.title("JH_Threading")
root.geometry("500x500")


stop_thread = False


progress_bar = ttk.Progressbar(root, orient = "horizontal", length = 200, mode = "determinate")
progress_bar.pack(pady = 10)

label_start = ttk.Label(root, text = "0%")
label_start.pack(pady = 10)


def block_gui():
    global stop_thread
    for i in range(101):      
        if stop_thread:
            break 
        progress_bar["value"] = i
        label_start.config(text = f"{i}%")
        root.update()
        progress_bar.step(1)
        time.sleep(1.2)


        
def start():
    global stop_thread
    stop_thread = False
    progress_bar["value"] = 0
    t = threading.Thread(target = block_gui)
    t.start()
    start_button.config(state = tk.DISABLED)
    stop_button.config(state = tk.NORMAL)
    

def stop():
    global stop_thread
    stop_thread = True
    progress_bar["value"] = 0
    label_start.config(text = "0%")
    start_button.config(state = tk.NORMAL)
    stop_button.config(state = tk.DISABLED)



start_button = ttk.Button(root, text = "Start", command = start)
start_button.pack(pady = 10)
start_button.config(state = tk.NORMAL)

stop_button = ttk.Button(root, text = "Stop", command = stop)
stop_button.pack(pady = 10)
stop_button.config(state = tk.DISABLED)


root.mainloop()
