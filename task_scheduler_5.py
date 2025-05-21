# task_scheduler_5.py
class Task:
    def __init__(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        if not self.head or self.head.priority < task.priority:
            task.next = self.head
            self.head = task
        else:
            current = self.head
            while current.next and current.next.priority >= task.priority:
                current = current.next
            task.next = current.next
            current.next = task

    def process_task(self):
        if self.head:
            task = self.head
            self.head = self.head.next
            return task
        return None

# Example usage
queue = PriorityQueue()
queue.add_task(Task("Task1", 2))
queue.add_task(Task("Task2", 1))
task = queue.process_task()
