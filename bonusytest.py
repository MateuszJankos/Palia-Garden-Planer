import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Słownik opisów warzyw
vegetable_descriptions = {
    1: "WP",
    2: "WP",
    3: "WR",
    4: "WR",
    5: "HB",
    6: "HB",
    7: "QB",
}

def on_button_click(row, col):
    global selected_vegetable
    if selected_vegetable is not None:
        # Jeśli wybrano warzywo, to ustaw je w danej komórce
        garden_plan[row][col] = selected_vegetable
        update_neighboring_cells(row, col)
    else:
        print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

def update_neighboring_cells(row, col):
    # Współrzędne sąsiednich pól
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    # Sprawdź każde sąsiednie pole i ustaw odpowiednie oznaczenia
    for r, c in neighbors:
        if 0 <= r < 9 and 0 <= c < 9:
            if garden_plan[r][c] is not None:
                # Jeśli pole jest już zasiane, to dodaj oznaczenie na podstawie wybranego warzywa
                description = vegetable_descriptions.get(garden_plan[r][c], "")
                garden_plan[r][c] = description
            else:
                # Jeśli pole jest puste, to dodaj oznaczenie na podstawie wybranego warzywa
                garden_plan[r][c] = vegetable_descriptions.get(selected_vegetable, "")

            # Aktualizuj oznaczenia na przycisku
            update_button_text(row, col)
            update_button_text(r, c)

def update_button_text(row, col):
    # Aktualizuj tekst na przycisku z uwzględnieniem oznaczenia
    description = garden_plan[row][col]
    if description:
        buttons[row][col].create_text(25, 25, text=description, fill="white", font=("Arial", 12))
    else:
        buttons[row][col].delete("all")  # Usuń tekst

def combine_vegetables(vegetable1, vegetable2):
    # Funkcja łącząca dwa warzywa w jedno, biorąc opisy z vegetable_descriptions
    description1 = vegetable_descriptions.get(vegetable1, "")
    description2 = vegetable_descriptions.get(vegetable2, "")
    combined_description = description1 + ", " + description2
    for veg, desc in vegetable_descriptions.items():
        if desc == combined_description:
            return veg
    return None
  # wybierz warzywo 
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
