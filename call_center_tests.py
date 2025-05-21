import unittest
from call_center_4 import Call, CallCenter

class TestCallCenter(unittest.TestCase):

    def test_receive_and_process_call(self):
        
        call_center = CallCenter()

       
        call1 = Call("123", "9:00 AM")
        call2 = Call("456", "9:05 AM")

      
        call_center.receive_call(call1)
        call_center.receive_call(call2)

        
        self.assertEqual(len(call_center.incoming_calls), 2)

        call_center.process_call()

        self.assertEqual(len(call_center.incoming_calls), 1)
        self.assertEqual(len(call_center.processing_calls), 1)


        finished_call = call_center.finish_call()
        

        self.assertEqual(finished_call.caller_id, "123")
        self.assertEqual(len(call_center.processing_calls), 0)

    def test_finish_call_when_no_call(self):
 
        call_center = CallCenter()

        finished_call = call_center.finish_call()
        self.assertIsNone(finished_call)

    def test_multiple_calls(self):

        call_center = CallCenter()


        call1 = Call("123", "9:00 AM")
        call2 = Call("456", "9:05 AM")
        call3 = Call("789", "9:10 AM")


        call_center.receive_call(call1)
        call_center.receive_call(call2)
        call_center.receive_call(call3)


        call_center.process_call()

        self.assertEqual(call_center.processing_calls[-1].caller_id, "123")


        call_center.finish_call()
        call_center.finish_call()

        self.assertEqual(len(call_center.processing_calls), 0)

def test_empty_queue(self):
 
    call_center = CallCenter()

    self.assertTrue(call_center.is_empty())


    call_center.receive_call(Call("123", "9:00 AM"))

    self.assertFalse(call_center.is_empty())


if __name__ == '__main__':
    unittest.main()
