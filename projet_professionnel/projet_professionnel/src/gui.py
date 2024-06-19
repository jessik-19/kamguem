import tkinter as tk
import customtkinter as ctk
from task_manager import TaskManager

def run_gui():
    manager = TaskManager()
    root = ctk.CTk()
    root.title("Gestionnaire de Tâches")

    # Champ de saisie pour la nouvelle tâche
    entry_task = ctk.CTkEntry(root, placeholder_text="Entrez une nouvelle tâche ici")
    entry_task.pack(pady=10)

    entry_date = ctk.CTkEntry(root, placeholder_text="Entrer la date de la tache (format jj/MM/AAAA) :")
    entry_date.pack(pady=10)

    # Fonction pour ajouter une tâche
    def add_task():
        task_description = entry_task.get()
        task_date = entry_date.get()
        if task_description and task_date:
            manager.add_task(task_description, task_date)
            entry_task.delete(0, 'end')
            entry_date.delete(0, 'end')  # Clear the input after adding
            list_tasks.insert('end', f"{task_description} - {task_date}")

    def remove_task():
        selected_index = list_tasks.curselection()
        if selected_index:
            manager.remove_task(selected_index[0])
            list_tasks.delete(selected_index[0])

    # Bouton pour ajouter la tâche
    button_add = ctk.CTkButton(root, text="Ajouter Tâche", command=add_task)
    button_add.pack(pady=20)

    button_add_1 = ctk.CTkButton(root, text="retirer Tâche", command=remove_task)
    button_add_1.pack(pady=20)

    # Liste pour afficher les tâches (utilisation de tkinter.Listbox)
    list_frame = ctk.CTkFrame(root)
    list_frame.pack(pady=20, fill='both', expand=True)
    list_tasks = tk.Listbox(list_frame, height=6)
    list_tasks.pack(side='left', fill='both', expand=True)
    for task in manager.tasks:
        list_tasks.insert('end', task.strip())

    root.mainloop()