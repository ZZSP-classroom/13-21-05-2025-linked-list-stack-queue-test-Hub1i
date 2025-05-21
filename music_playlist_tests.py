import unittest
from music_playlist_6 import Playlist, Song

class TestPlaylist(unittest.TestCase):

    def test_add_and_navigation(self):
        # Tworzymy playlistę
        playlist = Playlist()

        # Tworzymy piosenki
        song1 = Song("Song1", "Artist1")
        song2 = Song("Song2", "Artist2")
        song3 = Song("Song3", "Artist3")

        # Dodajemy piosenki do playlisty
        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)

        # Sprawdzamy, czy możemy przejść do następnej piosenki
        playlist.next_song()
        self.assertEqual(playlist.current_song.title, "Song2")

        # Sprawdzamy, czy możemy przejść do poprzedniej piosenki
        playlist.previous_song()
        self.assertEqual(playlist.current_song.title, "Song1")

if __name__ == '__main__':
    unittest.main()
