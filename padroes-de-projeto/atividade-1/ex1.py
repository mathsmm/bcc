from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("...")

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quacking!")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeaking!")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("...")


class Duck():
    def __init__(self) -> None:
        self.fly_behavior: FlyBehavior = None
        self.quack_behavior: QuackBehavior = None

    def swim(self):
        print("Swimming!")

    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior


class MallardDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Displaying a Mallard!")

class RedHeadDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Displaying a RedHead!")

class RubberDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Displaying a Rubberduck!")

class DecoyDuck(Duck):
    def __init__(self) -> None:
        super().__init__()

    def display(self):
        print("Displaying a Decoy duck!")


def main():
    fb1 = FlyWithWings()
    fb2 = FlyNoWay()

    qb1 = Quack()
    qb2 = Squeak()
    qb3 = MuteQuack()

    d1 = MallardDuck()
    d1.set_fly_behavior(fb1)   # Voa
    d1.set_quack_behavior(qb1) # Faz quack

    d2 = RedHeadDuck()
    d2.set_fly_behavior(fb1)   # Voa
    d2.set_quack_behavior(qb2) # Faz Squeak

    d3 = RubberDuck()
    d3.set_fly_behavior(fb2)   # Não voa
    d3.set_quack_behavior(qb1) # Faz quack

    d4 = DecoyDuck()
    d4.set_fly_behavior(fb2)   # Não voa
    d4.set_quack_behavior(qb3) # Não faz quack

    print("Comportamento do Mallard Duck")
    print("perform_fly: ", end="")
    d1.perform_fly()
    print("perform_quack: ", end="")
    d1.perform_quack()
    print()

    print("Comportamento do RedHead Duck")
    print("perform_fly: ", end="")
    d2.perform_fly()
    print("perform_quack: ", end="")
    d2.perform_quack()
    print()

    print("Comportamento do Rubber Duck")
    print("perform_fly: ", end="")
    d3.perform_fly()
    print("perform_quack: ", end="")
    d3.perform_quack()
    print()

    print("Comportamento do Decoy Duck")
    print("perform_fly: ", end="")
    d4.perform_fly()
    print("perform_quack: ", end="")
    d4.perform_quack()
    print()



if __name__ == "__main__":
    main()