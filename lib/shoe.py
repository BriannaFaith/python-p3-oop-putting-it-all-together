
#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition= "Worn"):
        self._brand = brand
        self._size = size
        self.condition = condition

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

adidas= Shoe("Adidas", 10)
adidas.size = 10
adidas.cobble()
print(adidas.condition)