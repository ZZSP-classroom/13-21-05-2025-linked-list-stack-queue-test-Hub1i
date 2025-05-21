# browser_history_3.py
class Page:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self):
        self.current = None

    def add_page(self, url):
        new_page = Page(url)
        if self.current:
            self.current.next = new_page
            new_page.prev = self.current
        self.current = new_page

    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next

    def get_current_page(self):
        return self.current.url if self.current else None

# Example usage
history = BrowserHistory()
history.add_page("google.com")
history.add_page("facebook.com")
history.add_page("twitter.com")

history.go_back()
print(history.get_current_page())  # Should show "facebook.com"
