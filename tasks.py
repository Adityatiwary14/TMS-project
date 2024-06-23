class TMS:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def get_all_tasks(self):
        return self.tasks

    def create_task(self, task):
        task['id'] = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task_by_id(self, task_id):
        task = next((task for task in self.tasks if task['id'] == task_id), None)
        return task

    def update_task(self, task_id, updated_task):
        task = self.get_task_by_id(task_id)
        if task:
            task.update(updated_task)
        return task

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
