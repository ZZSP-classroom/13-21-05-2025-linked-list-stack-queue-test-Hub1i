import unittest
from task_scheduler_5 import Task, PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_add_task_and_process(self):
        # Tworzymy zadania
        task1 = Task("Task1", 3)
        task2 = Task("Task2", 1)
        task3 = Task("Task3", 2)

        # Tworzymy kolejkę priorytetową
        pq = PriorityQueue()

        # Dodajemy zadania do kolejki
        pq.add_task(task1)
        pq.add_task(task2)
        pq.add_task(task3)

        # Sprawdzamy, czy kolejność zadań jest poprawna (na podstawie priorytetu)
        first_task = pq.process_task()
        self.assertEqual(first_task.task_name, "Task1")  # Task1 ma najwyższy priorytet

        second_task = pq.process_task()
        self.assertEqual(second_task.task_name, "Task3")  # Task3 ma średni priorytet

        third_task = pq.process_task()
        self.assertEqual(third_task.task_name, "Task2")  # Task2 ma najniższy priorytet

    def test_process_task_when_empty(self):
        # Tworzymy pustą kolejkę priorytetową
        pq = PriorityQueue()
        # Sprawdzamy, czy procesowanie zadania na pustej kolejce zwraca None
        task = pq.process_task()
        self.assertIsNone(task)

    def test_task_priority_order(self):
        # Tworzymy zadania
        task1 = Task("Task1", 5)
        task2 = Task("Task2", 2)
        task3 = Task("Task3", 8)

        pq = PriorityQueue()
        pq.add_task(task1)
        pq.add_task(task2)
        pq.add_task(task3)

        # Sprawdzamy kolejność zadań, zaczynając od najwyższego priorytetu
        first_task = pq.process_task()
        self.assertEqual(first_task.task_name, "Task3")  # Task3 ma najwyższy priorytet
        second_task = pq.process_task()
        self.assertEqual(second_task.task_name, "Task1")  # Task1 ma średni priorytet
        third_task = pq.process_task()
        self.assertEqual(third_task.task_name, "Task2")  # Task2 ma najniższy priorytet

if __name__ == '__main__':
    unittest.main()
