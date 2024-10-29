from pynput import keyboard
import tkinter as tk

# Define the remapping
remap = {
    '7': '7', '8': '8', '9': '9',
    'u': '4', 'i': '5', 'o': '6',
    'j': '1', 'k': '2', 'l': '3',
    'm': '0'
}

# Function to handle key press
def on_press(key):
    try:
        if key.char in remap:
            print(f"Remapped {key.char} to {remap[key.char]}")
    except AttributeError:
        pass

# Listener for keyboard events
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Simple GUI to enable/disable remapping
def toggle_remap():
    if listener.running:
        listener.stop()
        toggle_button.config(text="Enable 10-Key")
    else:
        listener.start()
        toggle_button.config(text="Disable 10-Key")

root = tk.Tk()
root.title("10-Key Remapper")
toggle_button = tk.Button(root, text="Enable 10-Key", command=toggle_remap)
toggle_button.pack(pady=20)
root.mainloop()
