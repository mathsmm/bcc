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

# INTERFACE
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


# CONCRETA
class WeatherData(Subject):
    def __init__(self, temperature: float, humidity: float, pressure: float) -> None:
        self.observers = set()
        self.__temperature: float = temperature
        self.__humidity: float = humidity
        self.__pressure: float = pressure

    def register_observer(self, observer: Observer):
        self.observers.add(observer)
        observer.subject = self

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
        observer.subject = None

    def notify_observers(self):
        for o in self.observers:
            o.update()

    # TEMPERATURA
    def get_temperature(self):
        return self.__temperature

    # UMIDADE
    def get_humidity(self):
        return self.__humidity

    # PRESSÃO
    def get_pressure(self):
        return self.__pressure

    def measurements_changed(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.notify_observers()


# CONCRETA
class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self) -> None:
        self.subject: Subject = None

    def update(self):
        self.display()

    def display(self):
        print(f"*CurrentConditionsDisplay -> Temp.: {self.subject.get_temperature()}, Hum.: {self.subject.get_humidity()}, Press.: {self.subject.get_pressure()}")

# CONCRETA
class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self) -> None:
        self.subject: Subject = None
        self.temperatures = list()
        self.humidities = list()
        self.pressures = list()

    def update(self):
        self.temperatures.append(self.subject.get_temperature())
        self.humidities.append(self.subject.get_humidity())
        self.pressures.append(self.subject.get_pressure())
        self.display()

    def avg(self, l: list):
        s = 0
        for v in l:
            s += v
        return s / len(l)

    def display(self):
        print(
            "*StatisticsDisplay:\n" + \
            f"Avg. temp.: {self.avg(self.temperatures)}, Avg hum.: {self.avg(self.humidities)}, Avg press.: {self.avg(self.pressures)}\n" + \
            f"Min. temp.: {min(self.temperatures)}, Min hum.: {min(self.humidities)}, Min press.: {min(self.pressures)}\n" + \
            f"Max. temp.: {max(self.temperatures)}, Max hum.: {max(self.humidities)}, Max press.: {max(self.pressures)}"
        )

# CONCRETA
class ThirdPartyDisplay(Observer, DisplayElement):
    def __init__(self) -> None:
        self.subject: Subject = None

    def update(self):
        self.display()

    def display(self):
        print(f"*ThirdPartyDisplay -> Only the pressure: {self.subject.get_pressure()}")

# CONCRETA
class ForecastDisplay(Observer, DisplayElement):
    def __init__(self) -> None:
        self.subject: Subject = None

    def update(self):
        self.display()

    def display(self):
        temp = self.subject.get_temperature()
        msg = ""
        if temp <= 15:
            msg = "Cold!"
        elif temp > 15 and temp <= 25:
            msg = "Cozy!"
        elif temp > 25 and temp <= 35:
            msg = "Hot!"
        elif temp > 35:
            msg = "Welcome to Blumenau!"
        print("*ForecastDisplay ->", msg)


# Cirando WeatherData
wd = WeatherData(0.00, 0.00, 0.00)

# Criando Displays
ccd = CurrentConditionsDisplay()
std = StatisticsDisplay()
tpd = ThirdPartyDisplay()
fcd = ForecastDisplay()

# Registrando Displays como observadores
wd.register_observer(ccd)
wd.register_observer(std)
wd.register_observer(tpd)
wd.register_observer(fcd)

print("==============================================================")
print("Atualizando WeatherData e executando displays pela PRIMEIRA vez")
wd.measurements_changed(21.0, 0.50, 1.0)

print("==============================================================")
print("Atualizando WeatherData e executando displays pela SEGUNDA vez")
wd.measurements_changed(30.0, 0.80, 1.1)

print("==============================================================")
print("Atualizando WeatherData e executando displays pela TERCEIRA vez")
wd.measurements_changed(38.0, 0.90, 1.2)