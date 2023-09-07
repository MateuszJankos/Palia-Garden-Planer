import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def on_button_click(row, col):
    if selected_vegetable is not None:
        # Jeśli wybrano warzywo, to ustaw jego obrazek na guziku
        if selected_vegetable in vegetable_images:
            buttons[row][col].configure(image=vegetable_images[selected_vegetable])
            garden_plan[row][col] = selected_vegetable
        else:
            print(f"Nie znaleziono obrazka dla warzywa {selected_vegetable}")
    else:
        print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

def select_vegetable(vegetable):
    global selected_vegetable
    selected_vegetable = vegetable

root = tk.Tk()
root.configure(bg='#303533')
root.geometry("600x800")
root.title("Palia Garden Planer Program")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

image = Image.open("soil.png")
photo = ImageTk.PhotoImage(image)

buttons = [[None for _ in range(9)] for _ in range(9)]
vegetable_images = {}

selected_vegetable = None  # Zmienna do przechowywania wybranego warzywa
garden_plan = [[None for _ in range(9)] for _ in range(9)]  # Tablica do przechowywania informacji o zasianych warzywach

for row in range(9):
    for col in range(9):
        button = tk.Button(frame, image=photo, width=50, height=50, command=lambda row=row, col=col: on_button_click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        buttons[row][col] = button  # Dodajemy guzik do tablicy guzików

label = tk.Label(root, text="Set up your garden here")
label.pack(pady=10)

# Tworzenie ramki dla 7 guzików poziomo
button_frame = tk.Frame(root)
button_frame.pack()

# Dodajemy 7 guzików z obrazkami od 1 do 7
for i in range(1, 8):
    digit_image = Image.open(f"{i}.png")
    digit_photo = ImageTk.PhotoImage(digit_image)
    vegetable_images[i] = digit_photo  # Przechowujemy obrazki warzyw w słowniku
    button = tk.Button(button_frame, image=digit_photo, width=50, height=50, command=lambda i=i: select_vegetable(i))
    button.pack(side=tk.LEFT, padx=5)

for i in range(9):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

root.mainloop()
