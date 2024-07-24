graus_celsius = 10

while graus_celsius <= 100:
    graus_fahrenheit = int((graus_celsius * 9 / 5) + 32)
    print(f"{graus_celsius}°C = {graus_fahrenheit}°F")
    graus_celsius += 10