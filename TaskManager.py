import datetime
from Task import Task
from TaskList import TaskList

class TaskManager:
    def __init__(self):
        self.task_lists = {"all": TaskList(), "completed": TaskList(), "active": TaskList()}
        self.load_tasks()

    def add_task(self, description, due_date, priority):
        task_key = f"{description}|{due_date}|{priority}"
        if task_key in self.get_task_keys():
            print("Це завдання вже існує.")
            return

        if not description:
            print("Опис не може бути порожнім.")
            return
        if len(description) > 100:
            print("Опис завдання занадто довгий.")
            return
        if not self.is_valid_date(due_date):
            print("Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД.")
            return
        if not 1 <= priority <= 5:
            print("Пріоритет повинен бути цілим числом від 1 до 5.")
            return

        new_task = Task(description, due_date, priority)
        
    
        self.task_lists["active"].add_task(new_task)
        self.save_tasks()

    def remove_task(self, index):
        try:
            task = self.task_lists["active"].tasks.pop(index)
            self.task_lists["all"].tasks.remove(task)
            print("Завдання успішно видалено.")
            self.save_tasks()
        except IndexError:
            print("Неправильний індекс завдання.")

    def complete_task(self, index):
        try:
            tasks = self.task_lists["active"].tasks
            tasks.sort(key=lambda x: x.priority)
            print(f"{'Індекс':<6} {'Опис':<30} {'По даті':<12} {'Пріоритет':<10} {'Статус':<10}")
            for i, task in enumerate(tasks):
                print(f"{i:<6} {task.description:<30} {task.due_date:<12} {task.priority:<10} {'Completed' if task.completed else 'Active'}")
                task = tasks[index]
                index = int(input("Введіть індекс завдання для завершення: "))

            if 0 <= index < len(tasks): 
                task.completed = True
                self.task_lists["active"].tasks.remove(task)
                self.task_lists["completed"].tasks.append(task)
                print("Завдання успішно завершено.")
                self.save_tasks()
            else:
                print("Неправильний індекс завдання.")
        except ValueError:
            print("Неправильний індекс завдання.")

    def view_tasks(self, status="all", sort_by="date"):
        if status not in ["1", "2", "3"]:
            print("Неправильний фільтр статусу.")
            return
        if sort_by not in ["1", "2"]:
            print("Неправильна опція сортування.")
            return

        statuses = {"1": "all", "2": "completed", "3": "active"}
        sorting = {"1": "due_date", "2": "priority"}

        tasks = self.task_lists[statuses[status]].tasks
        if sort_by == "1":
            tasks.sort(key=lambda x: getattr(x, sorting[sort_by]))
        elif sort_by == "2":
            tasks.sort(key=lambda x: x.priority)

        print(f"{'Індекс':<6} {'Опис':<30} {'Дата завершення':<12} {'Пріоритет':<10} {'Статус':<10}")
        for i, task in enumerate(tasks):
            print(f"{i:<6} {task.description:<30} {task.due_date:<12} {task.priority:<10} {'Завершено' if task.completed else 'Активне'}")

    def is_valid_date(self, date_string):
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def update_task(self, index, description=None, due_date=None, priority=None):
        try:
            task = self.task_lists["active"].tasks[index]
        except IndexError:
            print("Неправильний індекс завдання.")
            return

        if description:
            task.description = description
        if due_date:
            if self.is_valid_date(due_date):
                task.due_date = due_date
            else:
                print("Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД.")
                return
        if priority is not None:
            if 1 <= priority <= 5:
                task.priority = priority
            else:
                print("Пріоритет повинен бути цілим числом від 1 до 5.")
                return

        print("Інформація про завдання оновлена успішно.")
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task_list in self.task_lists.values():
                for task in task_list.tasks:
                    file.write(f"{task.description}|{task.due_date}|{task.priority}|{task.completed}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                for line in file:
                    description, due_date, priority, completed = line.strip().split("|")
                    new_task = Task(description, due_date, int(priority))
                    new_task.completed = completed == "True"
                    self.task_lists["all"].add_task(new_task)
                    if new_task.completed:
                        self.task_lists["completed"].add_task(new_task)
                    else:
                        self.task_lists["active"].add_task(new_task)
        except FileNotFoundError:
            pass

    def get_task_keys(self):
        task_keys = set()
        for task_list in self.task_lists.values():
            for task in task_list.tasks:
                task_key = f"{task.description}|{task.due_date}|{task.priority}"
                task_keys.add(task_key)
        return task_keys
