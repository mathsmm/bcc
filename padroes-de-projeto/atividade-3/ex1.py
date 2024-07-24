from abc import ABC, abstractmethod


# INTERFACE
class Beverage(ABC):
    def __init__(self) -> None:
        self.description = "Unknown beverage"

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# INTERFACE
class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# CONCRETA
class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = "House blend coffee"

    def get_description(self):
        return self.description

    def cost(self):
        return 0.89

# CONCRETA
class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description = "Dark roast coffee"

    def get_description(self):
        return self.description

    def cost(self):
        return 0.99

# CONCRETA
class Espresso(Beverage):
    def __init__(self) -> None:
        self.description = "Espresso coffee"

    def get_description(self):
        return self.description

    def cost(self):
        return 1.99

# CONCRETA
class Decaf(Beverage):
    def __init__(self) -> None:
        self.description = "Decaf coffee"

    def get_description(self):
        return self.description

    def cost(self):
        return 1.05

# CONCRETA
class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Milk"

    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()

# CONCRETA
class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Mocha"

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()

# CONCRETA
class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Soy"

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15+ self.beverage.cost()

# CONCRETA
class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage: Beverage = beverage
        self.description = "Whip"

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()


b1 = Espresso()
print(b1.get_description() + " $" + str(b1.cost()))

b2 = DarkRoast()
b2 = Mocha(b2)
b2 = Mocha(b2)
b2 = Whip(b2)
print(b2.get_description() + " $" + str(b2.cost()))

b3 = HouseBlend()
b3 = Soy(b3)
b3 = Mocha(b3)
b3 = Whip(b3)
print(b3.get_description() + " $" + str(b3.cost()))