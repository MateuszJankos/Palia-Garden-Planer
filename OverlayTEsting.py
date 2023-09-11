import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def on_button_click(row, col):
    if selected_vegetable is not None:
        # Jeśli wybrano warzywo, to ustaw jego obrazek na guziku
        if selected_vegetable in vegetable_images:
            buttons[row][col].configure(image=vegetable_images[selected_vegetable])
            garden_plan[row][col] = selected_vegetable
            apply_bonuses(row, col)
        else:
            print(f"Nie znaleziono obrazka dla warzywa {selected_vegetable}")
    else:
        print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

def apply_bonuses(row, col):
    # Sprawdź sąsiednie pola pionowo i poziomo
    neighbors = []
    if row > 0:
        neighbors.append(garden_plan[row - 1][col])  # Pole nad aktualnym
    if row < 8:
        neighbors.append(garden_plan[row + 1][col])  # Pole pod aktualnym
    if col > 0:
        neighbors.append(garden_plan[row][col - 1])  # Pole na lewo od aktualnego
    if col < 8:
        neighbors.append(garden_plan[row][col + 1])  # Pole na prawo od aktualnego

    # Sprawdź, które bonusy powinny być przyznane
    bonus = None
    if 1 in neighbors or 2 in neighbors:
        bonus = "Weed Prevention"
    elif 3 in neighbors or 4 in neighbors:
        bonus = "Water Retain"
    elif 5 in neighbors or 6 in neighbors:
        bonus = "Harvest boost"
    elif 7 in neighbors:
        bonus = "Quality boost"

    # Usuń istniejącą etykietę bonusu (jeśli istnieje)
    if bonus_labels[row][col]:
        bonus_labels[row][col].destroy()

    # Wyświetl bonusy na etykiecie nad obrazkiem
    if bonus:
        bonus_label = tk.Label(frame, text=bonus, font=("Helvetica", 10, "bold"), fg="green")
        bonus_label.grid(row=row, column=col, sticky="nsew")
        bonus_labels[row][col] = bonus_label  # Zapisz referencję do etykiety w tablicy

def select_vegetable(vegetable):
    global selected_vegetable
    selected_vegetable = vegetable

def reset_garden():
    global selected_vegetable, garden_plan
    selected_vegetable = None
    garden_plan = [[None for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            buttons[row][col].configure(image=photo)
            # Usuń etykietę z bonusami
            bonus_labels[row][col].destroy()

# Dodaj dodatkową tablicę do przechowywania etykiet z bonusami
bonus_labels = [[None for _ in range(9)] for _ in range(9)]
    
root = tk.Tk()
root.configure(bg='#303533')
root.geometry("600x800")
root.title("Palia Garden Planner Program")

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

reset_button = tk.Button(root, text="Reset", command=reset_garden)
reset_button.pack(pady=10)

for i in range(9):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

root.mainloop()