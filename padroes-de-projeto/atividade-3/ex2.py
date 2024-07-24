from abc import ABC, abstractmethod
from enum import Enum

class Size(Enum):
    P = -0.05 # Subtrai 5 centavos
    M = +0.00 # Preço normal
    G = +0.05 # Adiciona 5 centavos

# INTERFACE
class Beverage(ABC):
    def __init__(self) -> None:
        self.description = "Unknown beverage"
        self.size: Size = Size.P

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def set_size(self, size: str):
        pass

# INTERFACE
class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# CONCRETA
class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = "House blend coffee"
        self.size: Size = Size.P

    def get_description(self):
        return self.description
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.89 + self.get_size()

# CONCRETA
class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description = "Dark roast coffee"
        self.size: Size = Size.P

    def get_description(self):
        return self.description
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.99 + self.get_size()

# CONCRETA
class Espresso(Beverage):
    def __init__(self) -> None:
        self.description = "Espresso coffee"
        self.size: Size = Size.P

    def get_description(self):
        return self.description
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 1.99 + self.get_size()

# CONCRETA
class Decaf(Beverage):
    def __init__(self) -> None:
        self.description = "Decaf coffee"
        self.size: Size = Size.P

    def get_description(self):
        return self.description
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 1.05 + self.get_size()

# CONCRETA
class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Milk"
        self.size: Size = beverage.size

    def get_description(self):
        return self.beverage.get_description() + ", Milk"
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.10 + self.get_size() + self.beverage.cost()

# CONCRETA
class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Mocha"
        self.size: Size = beverage.size

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.20 + self.get_size() + self.beverage.cost()

# CONCRETA
class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Soy"
        self.size: Size = beverage.size

    def get_description(self):
        return self.beverage.get_description() + ", Soy"
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.15 + self.get_size() + self.beverage.cost()

# CONCRETA
class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Whip"
        self.size: Size = beverage.size

    def get_description(self):
        return self.beverage.get_description() + ", Whip"
    
    def get_size(self):
        return self.size.value

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.10 + self.get_size() + self.beverage.cost()


b1 = DarkRoast()
b1.set_size(Size.P)
b1 = Mocha(b1)
b1 = Soy(b1)
b1 = Whip(b1)
print("P SIZE " + b1.get_description() + " $" + f'{b1.cost():.2f}')

b2 = DarkRoast()
b2.set_size(Size.M)
b2 = Mocha(b2)
b2 = Soy(b2)
b2 = Whip(b2)
print("M SIZE " + b2.get_description() + " $" + f'{b2.cost():.2f}')

b3 = DarkRoast()
b3.set_size(Size.G)
b3 = Mocha(b3)
b3 = Soy(b3)
b3 = Whip(b3)
print("G SIZE " + b3.get_description() + " $" + f'{b3.cost():.2f}')