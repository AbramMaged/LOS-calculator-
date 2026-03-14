import tkinter as tk
import math

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Retro LOS Calculator")
root.geometry("620x480")
root.configure(bg="#7e63a6")

# ---------- HEADER ----------
header = tk.Frame(root, bg="#4bb0b7", height=60, highlightbackground="#1a1a1a", highlightthickness=4)
header.pack(fill="x")

title = tk.Label(
    header,
    text="📡  LINE OF SIGHT CALCULATOR",
    bg="#4bb0b7",
    fg="black",
    font=("Arial",18,"bold")
)
title.pack(pady=12)

# ---------- MAIN PANEL ----------
panel = tk.Frame(root, bg="#f2b35c", highlightbackground="#1a1a1a", highlightthickness=5)
panel.pack(padx=25, pady=25, fill="both", expand=True)

# ---------- INPUTS ----------
tk.Label(panel,text="Height 1",bg="#f2b35c",font=("Arial",13,"bold")).grid(row=0,column=0,pady=10)

h1_entry = tk.Entry(panel,width=18,font=("Arial",12),bg="#4bb0b7",bd=4)
h1_entry.grid(row=0,column=1)

tk.Label(panel,text="Height 2",bg="#f2b35c",font=("Arial",13,"bold")).grid(row=1,column=0,pady=10)

h2_entry = tk.Entry(panel,width=18,font=("Arial",12),bg="#4bb0b7",bd=4)
h2_entry.grid(row=1,column=1)

# ---------- UNITS ----------
unit = tk.StringVar(value="m")

unit_frame = tk.Frame(panel,bg="#f2b35c")
unit_frame.grid(row=2,columnspan=2,pady=10)

tk.Radiobutton(unit_frame,text="Meters",variable=unit,value="m",bg="#f2b35c",font=("Arial",11)).pack(side="left",padx=15)
tk.Radiobutton(unit_frame,text="Feet",variable=unit,value="f",bg="#f2b35c",font=("Arial",11)).pack(side="left",padx=15)

# ---------- RESULTS ----------
r1 = tk.StringVar()
r2 = tk.StringVar()
rt = tk.StringVar()

result_frame = tk.Frame(panel,bg="#f2b35c")
result_frame.grid(row=5,columnspan=2,pady=20)

def result_box(label,row,var):
    tk.Label(result_frame,text=label,bg="#f2b35c",font=("Arial",12,"bold")).grid(row=row,column=0,padx=10,pady=6)
    
    tk.Label(
        result_frame,
        textvariable=var,
        bg="#4bb0b7",
        fg="black",
        width=16,
        height=1,
        font=("Arial",12,"bold"),
        bd=4
    ).grid(row=row,column=1,padx=10)

result_box("Horizon 1",0,r1)
result_box("Horizon 2",1,r2)
result_box("Total LOS",2,rt)

# ---------- FUNCTIONS ----------
def calc():
    try:
        h1=float(h1_entry.get())
        h2=float(h2_entry.get())

        if unit.get()=="f":
            h1*=0.3048
            h2*=0.3048

        d1=3.57*math.sqrt(h1)
        d2=3.57*math.sqrt(h2)

        r1.set(f"{d1:.2f} km")
        r2.set(f"{d2:.2f} km")
        rt.set(f"{d1+d2:.2f} km")

    except:
        r1.set("Invalid")

def clear():
    h1_entry.delete(0,tk.END)
    h2_entry.delete(0,tk.END)
    r1.set("")
    r2.set("")
    rt.set("")

# ---------- BUTTONS ----------
button_frame=tk.Frame(panel,bg="#f2b35c")
button_frame.grid(row=3,columnspan=2,pady=15)

tk.Button(
    button_frame,
    text="CALCULATE",
    command=calc,
    bg="#d96aa5",
    width=14,
    font=("Arial",12,"bold"),
    bd=4
).grid(row=0,column=0,padx=10)

tk.Button(
    button_frame,
    text="CLEAR",
    command=clear,
    bg="#4bb0b7",
    width=14,
    font=("Arial",12,"bold"),
    bd=4
).grid(row=0,column=1,padx=10)

root.mainloop()