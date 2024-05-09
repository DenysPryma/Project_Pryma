class Task:
    ID = 0

    def __init__(self, description, due_date, priority):
        self.id = Task.ID
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

        Task.ID += 1
