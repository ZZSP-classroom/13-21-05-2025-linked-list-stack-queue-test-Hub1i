import unittest
from call_center_4 import Call, CallCenter

class TestCallCenter(unittest.TestCase):

    def test_receive_and_process_call(self):
        # Tworzymy centrum obsługi połączeń
        call_center = CallCenter()

        # Tworzymy połączenia
        call1 = Call("123", "9:00 AM")
        call2 = Call("456", "9:05 AM")

        # Otrzymujemy połączenia
        call_center.receive_call(call1)
        call_center.receive_call(call2)

        # Sprawdzamy, czy połączenia zostały dodane do kolejki
        self.assertEqual(len(call_center.incoming_calls), 2)

        # Przetwarzamy pierwsze połączenie
        call_center.process_call()

        # Sprawdzamy, czy połączenie zostało przeniesione do procesu
        self.assertEqual(len(call_center.incoming_calls), 1)
        self.assertEqual(len(call_center.processing_calls), 1)

        # Zakończenie przetwarzanego połączenia
        finished_call = call_center.finish_call()
        
        # Sprawdzamy, czy zakończono przetwarzanie połączenia
        self.assertEqual(finished_call.caller_id, "123")
        self.assertEqual(len(call_center.processing_calls), 0)

    def test_finish_call_when_no_call(self):
        # Tworzymy centrum obsługi połączeń
        call_center = CallCenter()

        # Sprawdzamy, czy próba zakończenia połączenia bez przetwarzanego połączenia zwróci None
        finished_call = call_center.finish_call()
        self.assertIsNone(finished_call)

    def test_multiple_calls(self):
        # Tworzymy centrum obsługi połączeń
        call_center = CallCenter()

        # Tworzymy połączenia
        call1 = Call("123", "9:00 AM")
        call2 = Call("456", "9:05 AM")
        call3 = Call("789", "9:10 AM")

        # Otrzymujemy połączenia
        call_center.receive_call(call1)
        call_center.receive_call(call2)
        call_center.receive_call(call3)

        # Przetwarzamy pierwsze połączenie
        call_center.process_call()

        # Sprawdzamy, czy kolejność połączeń w procesie jest odpowiednia
        self.assertEqual(call_center.processing_calls[-1].caller_id, "123")

        # Zakończenie przetwarzanych połączeń
        call_center.finish_call()
        call_center.finish_call()

        # Sprawdzamy, czy zostały jeszcze jakieś połączenia w procesie
        self.assertEqual(len(call_center.processing_calls), 0)

def test_empty_queue(self):
    # Tworzymy centrum obsługi połączeń
    call_center = CallCenter()

    # Sprawdzamy, czy kolejka połączeń przychodzących jest pusta
    self.assertTrue(call_center.is_empty())

    # Otrzymujemy połączenie
    call_center.receive_call(Call("123", "9:00 AM"))

    # Sprawdzamy, czy kolejka nie jest pusta
    self.assertFalse(call_center.is_empty())


if __name__ == '__main__':
    unittest.main()
