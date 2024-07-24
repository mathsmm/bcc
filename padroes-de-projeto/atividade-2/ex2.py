from abc import ABC, abstractmethod


# INTERFACE
class Subject(ABC):
    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# INTERFACE
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# CONCRETA
class Notifier:
    def notify_users(observers: Observer):
        for o in observers:
            o.update()

# CONCRETA
class Store(Subject):
    def __init__(self) -> None:
        self.observers = set()
        self.products = list()

    def register_observer(self, observer: Observer):
        self.observers.add(observer)
        observer.subject = self

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        observer.subject = None

    def notify_observers(self):
        Notifier.notify_users(self.observers)

    def add_product(self, product_value: int):
        self.products.append(product_value)
        self.notify_observers()

    def change_value(self, product_index: int, product_value: int):
        self.products[product_index] = product_value
        self.notify_observers()

# CONCRETA
class User(Observer):
    def __init__(self, nome: str) -> None:
        self.nome: str = nome

    def update(self):
        print(f"{self.nome} notificado(a)!")


s = Store()

u1 = User("Matheus")
u2 = User("Paulo")
u3 = User("Leandro")

s.register_observer(u1)
s.register_observer(u2)
s.register_observer(u3)

s.add_product(50)
s.add_product(100)
s.change_value(1, 130)