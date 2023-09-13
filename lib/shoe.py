#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="whatever") -> None:
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, (float, int)):
            self._size = value
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
