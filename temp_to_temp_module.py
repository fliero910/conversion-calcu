def celsius_to_fahrenheit(x):
    return x * (9/5) + 32

def celsius_to_kelvin(x):
    return x + 273.15

def fahrenheit_to_celsius(x):
    return (x - 32) * (5/9)

def fahrenheit_to_kelvin(x):
    return (x - 32) * (5/9) + 273.15

def kelvin_to_celsius(x):
    return x - 273.15

def kelvin_to_fahrenheit(x):
    return (x - 273.15) * (9/5) + 32

def display_menu():
    while True:
        print("\n🌡️ Temperature Conversion Menu 🌡️")
        print("\t1. Celsius to Fahrenheit")
        print("\t2. Celsius to Kelvin")
        print("\t3. Fahrenheit to Celsius")
        print("\t4. Fahrenheit to Kelvin")
        print("\t5. Kelvin to Celsius")
        print("\t6. Kelvin to Fahrenheit")
        print("\tType 'exit' to quit")

        choice = input("➡️ Choose a conversion (1-6): ")

        if choice == 'exit':
            print("Goodbye!")
            break

        if choice == '1':
            value = float(input("Enter value in Celsius: "))
            print(f"{value}°C is {celsius_to_fahrenheit(value)}°F.")
        elif choice == '2':
            value = float(input("Enter value in Celsius: "))
            print(f"{value}°C is {celsius_to_kelvin(value)}K.")
        elif choice == '3':
            value = float(input("Enter value in Fahrenheit: "))
            print(f"{value}°F is {fahrenheit_to_celsius(value)}°C.")
        elif choice == '4':
            value = float(input("Enter value in Fahrenheit: "))
            print(f"{value}°F is {fahrenheit_to_kelvin(value)}K.")
        elif choice == '5':
            value = float(input("Enter value in Kelvin: "))
            print(f"{value}K is {kelvin_to_celsius(value)}°C.")
        elif choice == '6':
            value = float(input("Enter value in Kelvin: "))
            print(f"{value}K is {kelvin_to_fahrenheit(value)}°F.")
        else:
            print("⚠️ Invalid choice. Please select a valid option.")
