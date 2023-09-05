import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def on_button_click(row, col):
    print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

root = tk.Tk()

# Wymiary okna
root.geometry("600x800")

#Tytuł Programu na górze
root.title("Palia Garden Planer Program")

# Tworzenie ramki do umieszczenia siatki guzików
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Wczytaj obraz i przekształć go na format obsługiwany przez Tkinter
image = Image.open("soil.png")
photo = ImageTk.PhotoImage(image)

# Tworzenie siatki guzików z obrazem
buttons = [[None for _ in range(9)] for _ in range(9)]

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

# Dodajemy 7 guzików z nazwami od 1 do 7 poziomo
for i in range(1, 8):
    button = tk.Button(button_frame, text=str(i), width=5, height=2)
    button.pack(side=tk.LEFT, padx=5)

# Uruchomienie pętli głównej
root.mainloop()