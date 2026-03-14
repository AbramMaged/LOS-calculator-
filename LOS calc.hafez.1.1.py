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



import tkinter as tk
import math

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("LOS Calculator")
root.geometry("400x450")
root.configure(bg="#1e1e1e")

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="Line Of Sight Calculator",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e1e",
    fg="#8d6de6"
)
title.pack(pady=15)

# ---------------- INPUT FRAME ----------------
input_frame = tk.Frame(root, bg="#131212")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Antenna Height 1", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=10, pady=5)

height1_entry = tk.Entry(
    input_frame,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=15
)
height1_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Antenna Height 2", bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=10, pady=5)

height2_entry = tk.Entry(
    input_frame,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    relief="flat",
    width=15
)
height2_entry.grid(row=1, column=1, pady=5)

# ---------------- UNITS ----------------
unit_var = tk.StringVar(value="meters")

unit_frame = tk.Frame(root, bg="#1e1e1e")
unit_frame.pack(pady=10)

tk.Radiobutton(
    unit_frame,
    text="Meters",
    variable=unit_var,
    value="meters",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2b2b2b"
).grid(row=0, column=0, padx=10)

tk.Radiobutton(
    unit_frame,
    text="Feet",
    variable=unit_var,
    value="feet",
    bg="#1e1e1e",
    fg="white",
    selectcolor="#2b2b2b"
).grid(row=0, column=1, padx=10)

# ---------------- RESULTS ----------------
result_frame = tk.Frame(root, bg="#1e1e1e")
result_frame.pack(pady=15)

result1_var = tk.StringVar()
result2_var = tk.StringVar()
total_var = tk.StringVar()

# Horizon 1
tk.Label(result_frame, text="Horizon 1", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="w", padx=5)

h1_box = tk.Label(
    result_frame,
    textvariable=result1_var,
    bg="#2b2b2b",
    fg="#7c4dff",
    font=("Segoe UI", 11, "bold"),
    width=15,
    pady=5
)
h1_box.grid(row=0, column=1, padx=10, pady=5)

# Horizon 2
tk.Label(result_frame, text="Horizon 2", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="w", padx=5)

h2_box = tk.Label(
    result_frame,
    textvariable=result2_var,
    bg="#2b2b2b",
    fg="#7c4dff",
    font=("Segoe UI", 11, "bold"),
    width=15,
    pady=5
)
h2_box.grid(row=1, column=1, padx=10, pady=5)

# Total LOS
tk.Label(result_frame, text="Total LOS", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="w", padx=5)

total_box = tk.Label(
    result_frame,
    textvariable=total_var,
    bg="#2b2b2b",
    fg="#7c4dff",
    font=("Segoe UI", 11, "bold"),
    width=15,
    pady=4
)
total_box.grid(row=2, column=1, padx=10, pady=5)
# ---------------- FUNCTIONS ----------------
def calculate_los():
    try:
        h1 = float(height1_entry.get())
        h2 = float(height2_entry.get())

        if unit_var.get() == "feet":
            h1 *= 0.3048
            h2 *= 0.3048

        d1 = 3.57 * math.sqrt(h1)
        d2 = 3.57 * math.sqrt(h2)
        total = d1 + d2

        result1_var.set(f"{d1:.2f} km")
        result2_var.set(f"{d2:.2f} km")
        total_var.set(f"{total:.2f} km")

    except:
        result1_var.set("Invalid input")
        result2_var.set("")
        total_var.set("")

def clear_fields():
    height1_entry.delete(0, tk.END)
    height2_entry.delete(0, tk.END)
    result1_var.set("")
    result2_var.set("")
    total_var.set("")

# ---------------- BUTTONS ----------------
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=15)

calc_btn = tk.Button(
    button_frame,
    text="Calculate",
    command=calculate_los,
    bg="#7c4dff",
    fg="white",
    relief="flat",
    width=12
)
calc_btn.grid(row=0, column=0, padx=10)

total_box = tk.Label(
    result_frame,
    textvariable=total_var,
    bg="#2b2b2b",
    fg="#7c4dff",
    font=("Segoe UI", 12, "bold"),
    width=15,
    pady=6,
    highlightbackground="#9c8acc",
    highlightthickness=1
)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    bg="#2b2b2b",
    fg="white",
    relief="flat",
    width=12
)
clear_btn.grid(row=0, column=1, padx=10)

# ---------------- RUN APP ----------------
root.mainloop()