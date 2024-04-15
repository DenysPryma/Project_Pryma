class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        return self.tasks.pop(index)

    def complete_task(self, index):
        task = self.tasks[index]
        task.completed = True
        return task
