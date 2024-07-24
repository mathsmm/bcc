from abc import ABC, abstractmethod
from src.body import Body
import itertools

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def first(self):
        pass

class BodyIterator(Iterator):
    def __init__(self, body_list: list) -> None:
        # Deve retornar pares de corpos (b1, b2), onde
        # cada corpo só é par de outro corpo uma única vez
        def get_pairs_len(body_list_length: int):
            return int((body_list_length**2 - body_list_length) / 2)

        combinations = itertools.combinations(body_list, 2)
        self.pairs = list()

        for pair in combinations:
            self.pairs.append(pair)

        self.len = get_pairs_len(len(body_list))
        self.index = 0

    def has_next(self) -> bool:
        if self.index < self.len:
            return True
        return False

    def next(self) -> Body:
        result = self.pairs[self.index]
        self.index += 1
        return result
    
    def first(self) -> None:
        self.index = 0