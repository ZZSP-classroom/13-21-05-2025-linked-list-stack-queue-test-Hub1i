# hospital_1.py
class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"{self.name} at {self.appointment_time}"

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

# Example usage
queue = Queue()
patient1 = Patient("John Doe", "10:00 AM")
patient2 = Patient("Jane Smith", "10:30 AM")
queue.enqueue(patient1)
queue.enqueue(patient2)

print(queue.peek())  # Should show John Doe's appointment

dequeued_patient = queue.dequeue()
print(f"Dequeued: {dequeued_patient}")  # Should show John Doe's appointment
