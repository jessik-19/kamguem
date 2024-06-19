from task_manager import TaskManager
from gui import run_gui

def main():
    choice = input("Choisissez l'interface (1: CLI, 2: GUI): ")
    if choice == '1':
        manager = TaskManager()
        while True:
            action = input("Que souhaitez-vous faire?\n\n (1: Ajouter une tâche \n2: Afficher les tâches \n3: Supprimer une tache, \n4: Quitter\n\n ): ")
            if action == '1':
                task_description = input("Entrez la description de la tâche : ")
                task_date = input("Entrer la date de la tache (format jj/MM/AAAA) :")
                manager.add_task(task_description,  task_date)
                print("Tâche ajoutée.")
            elif action == '2':
                for task in manager.tasks:
                    print(task)
            elif action == '3':
                manager.remove_task(int(input("Entrez l'index de la tâche à supprimer: ")))
            elif action == '4':
                print("Au revoir!")
                break
            else:
                print("Option non valide. Veuillez entrer 1, 2, 3 ou 4.")
    elif choice == '2':
        run_gui()
    else:
        print("Choix non valide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()