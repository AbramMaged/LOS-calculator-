import tkinter as tk
import math

# ----- CALCULATE FUNCTION -----
def calculate_los():
    try:
        h1 = float(height1_entry.get())
        h2 = float(height2_entry.get())

        unit = unit_var.get()

        # convert feet to meters
        if unit == "feet":
            h1 = h1 * 0.3048
            h2 = h2 * 0.3048

        d1 = 3.57 * math.sqrt(h1)
        d2 = 3.57 * math.sqrt(h2)
        total = d1 + d2

        result1_var.set(f"{d1:.2f} Km")
        result2_var.set(f"{d2:.2f} Km")
        total_var.set(f"{total:.2f} Km")

    except:
        result1_var.set("Invalid input")
        result2_var.set("")
        total_var.set("")


# ----- CLEAR FUNCTION -----
def clear_fields():
    height1_entry.delete(0, tk.END)
    height2_entry.delete(0, tk.END)
    result1_var.set("")
    result2_var.set("")
    total_var.set("")



# ----- MAIN WINDOW -----
root = tk.Tk()
root.title("Line Of Sight Calculator")
root.geometry("350x400")
#------ UNITS -----
unit_var = tk.StringVar(value="meters")

tk.Label(root, text="Units").pack()

tk.Radiobutton(root, text="Meters", variable=unit_var, value="meters").pack()
tk.Radiobutton(root, text="Feet", variable=unit_var, value="feet").pack()

# ----- INPUT SECTION -----
tk.Label(root, text="Antenna Height (1st Station)").pack()

height1_entry = tk.Entry(root)
height1_entry.pack()

tk.Label(root, text="Antenna Height (2nd Station)").pack()

height2_entry = tk.Entry(root)
height2_entry.pack()

# ----- BUTTONS -----
tk.Button(root, text="Calculate", command=calculate_los).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack()

# ----- RESULTS -----
tk.Label(root, text="Radio Horizon (1st Station)").pack()

result1_var = tk.StringVar()
tk.Label(root, textvariable=result1_var).pack()

tk.Label(root, text="Radio Horizon (2nd Station)").pack()

result2_var = tk.StringVar()
tk.Label(root, textvariable=result2_var).pack()

tk.Label(root, text="Total Line of Sight").pack()

total_var = tk.StringVar()
tk.Label(root, textvariable=total_var).pack()

# ----- RUN PROGRAM -----
root.mainloop()