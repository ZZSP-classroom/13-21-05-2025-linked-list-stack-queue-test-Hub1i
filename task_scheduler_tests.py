import unittest
from task_scheduler_5 import Task, PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_add_task_and_process(self):

        task1 = Task("Task1", 3)
        task2 = Task("Task2", 1)
        task3 = Task("Task3", 2)


        pq = PriorityQueue()


        pq.add_task(task1)
        pq.add_task(task2)
        pq.add_task(task3)

        first_task = pq.process_task()
        self.assertEqual(first_task.task_name, "Task1")

        second_task = pq.process_task()
        self.assertEqual(second_task.task_name, "Task3")  

        third_task = pq.process_task()
        self.assertEqual(third_task.task_name, "Task2")

    def test_process_task_when_empty(self):

        pq = PriorityQueue()

        task = pq.process_task()
        self.assertIsNone(task)

    def test_task_priority_order(self):

        task1 = Task("Task1", 5)
        task2 = Task("Task2", 2)
        task3 = Task("Task3", 8)

        pq = PriorityQueue()
        pq.add_task(task1)
        pq.add_task(task2)
        pq.add_task(task3)


        first_task = pq.process_task()
        self.assertEqual(first_task.task_name, "Task3")  
        second_task = pq.process_task()
        self.assertEqual(second_task.task_name, "Task1")  
        third_task = pq.process_task()
        self.assertEqual(third_task.task_name, "Task2") 

if __name__ == '__main__':
    unittest.main()
