#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        """page_count must be an integer"""
        if isinstance(page_count, int):
            self._page_count = page_count
            return self._page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Flipping the page...wow, you read fast!"""
        print("Flipping the page...wow, you read fast!")

book = Book("And Then There Were None", 452)
book.page_count = 344
book.turn_page()
        