class Vect:
    """
    A class that represents a vector of n dimensions
    """
    def __init__(self, *args: float) -> None:
        """
        Initiates a Vect object from a list of coordinates which 
        represents a vector in a given space.\n 
        The number of dimensions of the space is the number of arguments
        """
        self.coords = args
        self.dims = len(args)

    def __str__(self):
        result = ""
        i = 0
        while i < self.dims - 1:
            result += f"{self.coords[i]}, "
            i += 1
        return "<" + result + str(self.coords[i]) + ">"

    def __add__(self, v):
        if isinstance(v, Vect):
            new_coords_list = []
            i = 0
            while i < self.dims:
                new_coords_list.append(self.coords[i] + v.coords[i])
                i += 1
            return Vect(new_coords_list)

    def __sub__(self, v):
        if isinstance(v, Vect):
            new_coords_list = []
            i = 0
            while i < self.dims:
                new_coords_list.append(self.coords[i] - v.coords[i])
                i += 1
            return Vect(new_coords_list)

    def __mul__(self, v):
        if isinstance(v, float):
            new_coords_list = []
            i = 0
            while i < self.dims:
                new_coords_list.append(v * self.coords[i])
            return Vect(new_coords_list)

        if isinstance(v, Vect):
            result = 0.0
            i = 0
            while i < self.dims:
                result += self.coords[i] * v.coords[i]
                i += 1
            return result

    


def main():
    u = Vect(2, 3)
    v = Vect(1, 1)
    print(u - v)

if __name__ == "__main__":
    main()