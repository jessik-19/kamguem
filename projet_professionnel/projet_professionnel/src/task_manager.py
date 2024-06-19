class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = file.readlines()
        except FileNotFoundError:
            print("Aucun fichier de tâches trouvé. Un nouveau sera créé.")
        except Exception as e:
            #initialisation des taches pour s'assurer qu'il est toujours defini
            self.tasks = []

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(f"{task[0]}|{task[1]}\n")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de taches : {e}")

    def add_task(self, task, date):
        self.tasks.append([task, date])
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Index invalide, aucune tâche supprimée.")

    # Autres méthodes pour gérer les tâches