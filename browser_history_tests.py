import unittest
from browser_history_3 import BrowserHistory

class TestBrowserHistory(unittest.TestCase):

    def test_navigation(self):
        history = BrowserHistory()
        history.add_page("google.com")
        history.add_page("facebook.com")
        history.add_page("twitter.com")
        
        history.go_back()
        self.assertEqual(history.get_current_page(), "facebook.com")
        
        history.go_forward()
        self.assertEqual(history.get_current_page(), "twitter.com")

if __name__ == '__main__':
    unittest.main()
