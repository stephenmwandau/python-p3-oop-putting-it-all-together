    #!/usr/bin/env python3


class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        """says that the shoe has been repaired."""
        print("Your shoe is as good as new!")
        self.condition = "New"

stan_smith = Shoe("Nike", 9)
stan_smith.size = 8
stan_smith.cobble()
stan_smith.condition