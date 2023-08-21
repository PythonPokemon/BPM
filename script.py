import tkinter as tk
from tkinter import messagebox

def create_process():
    process_name = process_name_entry.get()
    # Hier könnten Sie den Geschäftsprozess erstellen und speichern
    messagebox.showinfo("Erfolg", f"Geschäftsprozess '{process_name}' wurde erstellt!")

# Hauptfenster erstellen
root = tk.Tk()
root.title("BPM-Anwendung")

# Eingabefeld für Prozessnamen
process_name_label = tk.Label(root, text="Prozessname:")
process_name_label.pack()

process_name_entry = tk.Entry(root)
process_name_entry.pack()

# Schaltfläche zum Erstellen eines Prozesses
create_button = tk.Button(root, text="Prozess erstellen", command=create_process)
create_button.pack()

# Schleife für die Anzeige des Fensters
root.mainloop()
