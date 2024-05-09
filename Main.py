
from TaskManager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nСистема управління завданнями")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Завершити завдання")
        print("4. Переглянути завдання")
        print("5. Оновити інформацію про завдання")
        print("6. Переглянути видалені завдання")
        print("7. Вийти з програми")

        choice = input("Введіть ваш вибір: ")

        if choice == "1":
            description = input("Введіть опис завдання: ")
            due_date = input("Введіть дату завершення (РРРР-ММ-ДД): ")
            priority = int(input("Введіть пріоритет (1-5): "))
            manager.add_task(description, due_date, priority)
        elif choice == "2":
            manager.view_tasks(status="1", sort_by="1")
            index = int(input("Введіть індекс завдання для видалення: "))
            manager.remove_task(index)
        elif choice == "3":
            manager.view_tasks(status="1", sort_by="1")
            index = int(input("Введіть індекс завдання для завершення: "))
            manager.complete_task(index)
        elif choice == "4":
            status = input("Введіть фільтр статусу (1-всі/2-завершені/3-активні): ")
            sort_by = input("Введіть опцію сортування (1-дата/2-пріоритет): ")
            manager.view_tasks(status, sort_by)
        elif choice == "5":
            manager.view_tasks(status="1", sort_by="1")
            index = int(input("Введіть індекс завдання для оновлення: "))
            description = input("Введіть новий опис завдання (натисніть Enter, щоб залишити без змін): ")
            due_date = input("Введіть нову дату завершення (РРРР-ММ-ДД) (натисніть Enter, щоб залишити без змін): ")
            priority = input("Введіть новий пріоритет (1-5) (натисніть Enter, щоб залишити без змін): ")
            if priority:
                priority = int(priority)
            manager.update_task(index, description, due_date, priority)
        elif choice == "6":
            manager.view_deleted_tasks()
        elif choice == "7":
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    main()
