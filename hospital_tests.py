import unittest
from hospital_1 import Queue, Patient

class TestHospitalQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        queue = Queue()
        patient1 = Patient("John Doe", "10:00 AM")
        patient2 = Patient("Jane Smith", "10:30 AM")
        
        queue.enqueue(patient1)
        queue.enqueue(patient2)
        
        self.assertEqual(queue.dequeue(), patient1)
        self.assertEqual(queue.dequeue(), patient2)
        
    def test_peek(self):
        queue = Queue()
        patient = Patient("John Doe", "10:00 AM")
        queue.enqueue(patient)
        
        self.assertEqual(queue.peek(), patient)
        
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        patient = Patient("John Doe", "10:00 AM")
        queue.enqueue(patient)
        self.assertFalse(queue.is_empty())

if __name__ == '__main__':
    unittest.main()
