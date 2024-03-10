#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count

    @property
    def title(self):
        return self._title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
