class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.current_song = None  # Atrybut do śledzenia bieżącej piosenki

    def add_song(self, song):
        if not self.head:
            self.head = song
            self.current_song = song  # Ustawiamy pierwszą piosenkę jako bieżącą
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = song

    def remove_song(self, title):
        if not self.head:
            return

        current = self.head
        if current.title == title:
            self.head = current.next
            if self.head is None:
                self.current_song = None  # Brak piosenek
            return

        prev = None
        while current:
            if current.title == title:
                if prev:
                    prev.next = current.next
                if current == self.current_song:
                    self.current_song = current.next  # Ustawiamy kolejną piosenkę jako bieżącą
                return
            prev = current
            current = current.next

    def next_song(self):
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
        return self.current_song

    def previous_song(self):
        if not self.current_song:
            return None
        current = self.head
        while current and current.next != self.current_song:
            current = current.next
        if current:
            self.current_song = current
        return self.current_song

    def print_playlist(self):
        current = self.head
        while current:
            print(f"Title: {current.title}, Artist: {current.artist}")
            current = current.next
