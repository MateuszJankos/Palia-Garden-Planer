import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame

def on_button_click(row, col):
    if selected_vegetable is not None:
        # Jeśli wybrano warzywo, to ustaw jego obrazek na guziku
        if selected_vegetable in vegetable_images:
            buttons[row][col].configure(image=vegetable_images[selected_vegetable])
            garden_plan[row][col] = selected_vegetable
            pygame.mixer.Sound("sound.mp3").play()  # Dodaj dźwięk po kliknięciu w pole
        else:
            print(f"Nie znaleziono obrazka dla warzywa {selected_vegetable}")
    else:
        print(f"Kliknięto przycisk w rzędzie {row}, kolumnie {col}")

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

def on_left_click(event):
    pygame.mixer.Sound("srclick.mp3").play()  # Dodaj dźwięk po lewym kliknięciu myszą

# Inicjowanie modułu dźwięku pygame.mixer
pygame.mixer.init()

root = tk.Tk()
root.geometry("720x720")
root.title("Palia Garden Planner Program")

# Dodaj tło jako obrazek Tlo.png
bg_image = Image.open("Tlo.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

label = tk.Label(root, text="Garden")
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(padx=20, pady=5)

image = Image.open("soil.png")
photo = ImageTk.PhotoImage(image)

buttons = [[None for _ in range(9)] for _ in range(9)]
vegetable_images = {}

selected_vegetable = None
garden_plan = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        button = tk.Button(frame, image=photo, width=50, height=50, command=lambda row=row, col=col: on_button_click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        buttons[row][col] = button

label = tk.Label(root, text="Set up your garden here")
label.pack(pady=5)

label = tk.Label(root, text="Crops")
label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack()

for i in range(1, 8):
    digit_image = Image.open(f"{i}.png")
    digit_photo = ImageTk.PhotoImage(digit_image)
    vegetable_images[i] = digit_photo
    button = tk.Button(button_frame, image=digit_photo, width=50, height=50, command=lambda i=i: select_vegetable(i))
    button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(root, text="Reset", command=reset_garden)
reset_button.pack(pady=10)

for i in range(9):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)

root.bind("<Button-1>", on_left_click)  # Przypisz dźwięk do lewego kliknięcia myszą

root.mainloop()

