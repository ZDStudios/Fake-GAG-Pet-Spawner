import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time
import subprocess

# 🌟 Elite Pet List (customizable)
PETS = [
    "Kisuna", "Panda", "Jandel-Monkey", "Butterfly", "Dragonfly",
    "Golden Goose", "Mimic-Octopus", "Blood-Hedgehog", "Frog", "Mole",
    "Bold-Eagle", "Sand-Snake", "Crystal Moth", "Axolotl",
    "Griffin", "Disco-Bee", "Red-Fox"
]

def is_roblox_running():
    return any("RobloxPlayerBeta.exe" in p.name() for p in psutil.process_iter())

def update_status():
    while True:
        running = is_roblox_running()
        status_light.config(bg="lime" if running else "gray")
        online_label.config(text="Online" if running else "Offline", fg="lime" if running else "red")
        time.sleep(2)

def spawn_pet():
    pet = pet_var.get()
    age = age_var.get()
    size = size_var.get()
    if not age or not size:
        status_label.config(text="⚠️ Enter age and size.")
        return
    status_label.config(text=f"Spawning {pet} (Age: {age}, Size: {size})...")
    root.after(1000, lambda: status_label.config(text="Loading..."))
    root.after(3000, lambda: status_label.config(text="Haha get hacked 😎"))

def open_roblox():
    try:
        subprocess.Popen("start roblox://", shell=True)
        status_label.config(text="Launching Roblox...")
    except Exception as e:
        status_label.config(text=f"Error: {e}")

def stream_code():
    lines = [
        "[PetSpanwer] Initializing overlay...",
        "[PetSpanwer] Checking Roblox status...",
        "[PetSpanwer] Loading pet modules...",
        "[PetSpanwer] Ready for spawn injection...",
        "[PetSpanwer] Awaiting user input..."
    ]
    i = 0
    while True:
        code_box.insert(tk.END, lines[i % len(lines)] + "\n")
        code_box.see(tk.END)
        i += 1
        time.sleep(1.5)

# 🖥️ UI Setup
root = tk.Tk()
root.title("🐾 Pet Spanwer")
root.geometry("700x400")
root.configure(bg="#0f0f0f")

# Title
title = tk.Label(root, text="PET SPANWER", font=("Orbitron", 22), fg="#00ffff", bg="#0f0f0f")
title.place(x=20, y=10)

# Status light
status_light = tk.Label(root, width=2, height=1, bg="gray", relief="sunken")
status_light.place(x=660, y=10)

# Online label
online_label = tk.Label(root, text="Offline", font=("Consolas", 10), fg="red", bg="#0f0f0f")
online_label.place(x=620, y=10)

# Pet dropdown
pet_var = tk.StringVar(value=PETS[0])
pet_menu = ttk.Combobox(root, textvariable=pet_var, values=PETS, font=("Consolas", 12), state="readonly", width=30)
pet_menu.place(x=20, y=60)

# Age input
age_var = tk.StringVar()
age_entry = tk.Entry(root, textvariable=age_var, font=("Consolas", 12), width=30)
age_entry.insert(0, "Enter age")
age_entry.place(x=20, y=100)

# Size input
size_var = tk.StringVar()
size_entry = tk.Entry(root, textvariable=size_var, font=("Consolas", 12), width=30)
size_entry.insert(0, "Enter size")
size_entry.place(x=20, y=140)

# Spawn button
spawn_btn = tk.Button(root, text="Spawn Pet", command=spawn_pet, font=("Consolas", 12), bg="#222", fg="#0f0")
spawn_btn.place(x=20, y=180)

# Open Roblox button
open_btn = tk.Button(root, text="Open Roblox", command=open_roblox, font=("Consolas", 12), bg="#104", fg="#00f")
open_btn.place(x=150, y=180)

# Status label
status_label = tk.Label(root, text="", font=("Consolas", 12), fg="#ff00ff", bg="#0f0f0f")
status_label.place(x=20, y=220)

# Code stream box
code_box = tk.Text(root, width=40, height=20, bg="#111", fg="#0ff", font=("Courier", 10))
code_box.place(x=350, y=50)

# Threads
threading.Thread(target=update_status, daemon=True).start()
threading.Thread(target=stream_code, daemon=True).start()

root.mainloop()
