import tkinter as tk
from PIL import Image, ImageTk

def on_button_click(row, col):
    print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

root = tk.Tk()

# Wymiary okna
root.geometry("600x800")

# Tytuł Programu na górze
root.title("Palia Garden Planer Program")

# Tworzenie ramki do umieszczenia guzików
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Tworzenie siatki guzików
buttons = [[None for _ in range(9)] for _ in range(9)]

# Przygotuj listę ścieżek do obrazków
image_paths = ["Carrot_Icon.png", "Onion_Icon.png", "Potato_Icon.png", "Tomato_Icon.png", "Wheat_Icon.png", "Rice_Icon.png", "Cotton_Icon.png"]

for row in range(9):
    for col in range(9):
        if 1 <= row * 9 + col + 1 <= 7:
            # Przygotowanie obrazka z pliku
            number_image = Image.open(image_paths[row * 9 + col])
            number_photo = ImageTk.PhotoImage(number_image)

            button = tk.Button(frame, image=number_photo, width=50, height=50, command=lambda row=row, col=col: on_button_click(row, col))
            button.image = number_photo  # Zachowujemy referencję do obrazka, aby nie został usunięty przez garbage collector
            button.grid(row=row, column=col, sticky="nsew")
        else:
            button = tk.Button(frame, text="", width=50, height=50)
            button.grid(row=row, column=col, sticky="nsew")

# Konfigurujemy rozciąganie siatki guzików w ramce
for i in range(9):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

# Dodajemy etykietę pod siatką guzików
label = tk.Label(root, text="Set up your garden here")
label.pack(pady=10)

# Uruchomienie pętli głównej
root.mainloop()