import tkinter as tk

root = tk.Tk()

root.geometry("600x800") # Wymiary okna
root.title("Palia Garden Planer Program") #Tytuł Programu na górze

label = tk.Label(root, text="Set up your garden here", font=('Arial', 18)) #root jako tekst oraz personalizacja tekstu
label.pack(padx=20, pady=20) #odstępy od krawędzi

root.mainloop()