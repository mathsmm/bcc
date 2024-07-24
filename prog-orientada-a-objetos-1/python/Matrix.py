class Matrix:
    """
    A class that represents a matrix of n rows and n columns
    """
    def __init__(self, values: list) -> None:
        self.rows = len(values)
        self.cols = len(values[0])