class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received


class CallCenter:
    def __init__(self):
        self.incoming_calls = []  # Kolejka dla połączeń przychodzących
        self.processing_calls = []  # Stos dla połączeń w trakcie obsługi

    def receive_call(self, call):
        """Dodaje połączenie do kolejki przychodzących połączeń"""
        self.incoming_calls.append(call)

    def process_call(self):
        """Przenosi połączenie z kolejki przychodzących do stosu przetwarzanych połączeń"""
        if self.incoming_calls:
            call = self.incoming_calls.pop(0)
            self.processing_calls.append(call)

    def finish_call(self):
        """Zakończenie przetwarzanego połączenia - przenosi połączenie ze stosu do zakończonych połączeń"""
        if self.processing_calls:
            return self.processing_calls.pop()
        return None

    def is_empty(self):
        """Sprawdza, czy kolejka przychodzących połączeń jest pusta"""
        return len(self.incoming_calls) == 0
