import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def on_button_click(row, col):
    if my_buttons[row][col]['state'] == 'normal':
        my_buttons[row][col]['state'] = 'disabled'
        my_buttons[row][col].config(relief=tk.SUNKEN, borderwidth=3)  # Ustaw obramówkę na klikniętym przycisku
        print(f"Zaznaczono przycisk w rzędzie {row}, kolumnie {col}")
    else:
        my_buttons[row][col]['state'] = 'normal'
        my_buttons[row][col].config(relief=tk.RAISED, borderwidth=1)  # Przywróć standardową obramówkę na odznaczonym przycisku
        print(f"Odznaczono przycisk w rzędzie {row}, kolumnie {col}")

root = tk.Tk()

# Zmiana koloru tła
root.configure(bg='#303533')

# Wymiary okna
root.geometry("600x800")

# Tytuł Programu na górze
root.title("Palia Garden Planer Program")

# Tworzenie ramki do umieszczenia siatki guzików
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Wczytaj obraz i przekształć go na format obsługiwany przez Tkinter
image = Image.open("soil.png")
photo = ImageTk.PhotoImage(image)

# Tworzenie siatki guzików z obrazem
my_buttons = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        button = tk.Button(frame, image=photo, width=50, height=50, command=lambda row=row, col=col: on_button_click(row, col))
        button.grid(row=row, column=col, sticky="nsew") # Ustawiamy sticky na "nsew" dla każdego guzika

# Konfigurujemy rozciąganie siatki guzików w ramce
for i in range(9):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

# Dodajemy etykietę pod siatką guzików
label = tk.Label(root, text="Set up your garden here")
label.pack(pady=10)  # Dodajemy odstęp od etykiety do siatki guzików

# Tworzymy ramkę dla 7 guzików poziomo
button_frame = tk.Frame(root)
button_frame.pack()

# Dodajemy 7 guzików z obrazkami od 1 do 7
for i in range(1, 8):
    # Wczytaj obrazek dla cyfry i przekształć go
    digit_image = Image.open(f"{i}.png")
    digit_photo = ImageTk.PhotoImage(digit_image)
    button = tk.Button(button_frame, image=digit_photo, width=65, height=65)
    button.image = digit_photo  # Zachowujemy referencję do obrazka
    button.pack(side=tk.LEFT, padx=5)

# Uruchomienie pętli głównej
root.mainloop()
