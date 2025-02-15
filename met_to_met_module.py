def kilometer_to_meter(value): return value * 1000
def kilometer_to_hectometer(value): return value * 10
def kilometer_to_decameter(value): return value * 100
def kilometer_to_decimeter(value): return value * 10000
def kilometer_to_centimeter(value): return value * 100000
def kilometer_to_millimeter(value): return value * 1000000

def hectometer_to_kilometer(value): return value / 10
def hectometer_to_meter(value): return value * 100
def hectometer_to_decameter(value): return value * 10
def hectometer_to_decimeter(value): return value * 1000
def hectometer_to_centimeter(value): return value * 10000
def hectometer_to_millimeter(value): return value * 100000

def decameter_to_kilometer(value): return value / 100
def decameter_to_hectometer(value): return value / 10
def decameter_to_meter(value): return value * 10
def decameter_to_decimeter(value): return value * 100
def decameter_to_centimeter(value): return value * 1000
def decameter_to_millimeter(value): return value * 10000

def meter_to_kilometer(value): return value / 1000
def meter_to_hectometer(value): return value / 100
def meter_to_decameter(value): return value / 10
def meter_to_decimeter(value): return value * 10
def meter_to_centimeter(value): return value * 100
def meter_to_millimeter(value): return value * 1000

def decimeter_to_meter(value): return value / 10
def decimeter_to_kilometer(value): return value / 10000
def decimeter_to_hectometer(value): return value / 1000
def decimeter_to_decameter(value): return value / 100
def decimeter_to_centimeter(value): return value * 10
def decimeter_to_millimeter(value): return value * 100

def centimeter_to_meter(value): return value / 100
def centimeter_to_kilometer(value): return value / 100000
def centimeter_to_hectometer(value): return value / 10000
def centimeter_to_decameter(value): return value / 1000
def centimeter_to_decimeter(value): return value / 10
def centimeter_to_millimeter(value): return value * 10

def millimeter_to_meter(value): return value / 1000
def millimeter_to_kilometer(value): return value / 1000000
def millimeter_to_hectometer(value): return value / 100000
def millimeter_to_decameter(value): return value / 10000
def millimeter_to_decimeter(value): return value / 100
def millimeter_to_centimeter(value): return value / 10


def display_menu():
    while True:
        print("\n🌟 Metric to Metric Conversions 🌟")
        print("\t1. Kilometer to Meter")
        print("\t2. Kilometer to Hectometer")
        print("\t3. Kilometer to Decameter")
        print("\t4. Kilometer to Decimeter")
        print("\t5. Kilometer to Centimeter")
        print("\t6. Kilometer to Millimeter")
        print("\t7. Hectometer to Kilometer")
        print("\t8. Hectometer to Meter")
        print("\t9. Hectometer to Decameter")
        print("\t10. Hectometer to Decimeter")
        print("\t11. Hectometer to Centimeter")
        print("\t12. Hectometer to Millimeter")
        print("\t13. Decameter to Kilometer")
        print("\t14. Decameter to Hectometer")
        print("\t15. Decameter to Meter")
        print("\t16. Decameter to Decimeter")
        print("\t17. Decameter to Centimeter")
        print("\t18. Decameter to Millimeter")
        print("\t19. Meter to Kilometer")
        print("\t20. Meter to Hectometer")
        print("\t21. Meter to Decameter")
        print("\t22. Meter to Decimeter")
        print("\t23. Meter to Centimeter")
        print("\t24. Meter to Millimeter")
        print("\t25. Decimeter to Meter")
        print("\t26. Decimeter to Kilometer")
        print("\t27. Decimeter to Hectometer")
        print("\t28. Decimeter to Decameter")
        print("\t29. Decimeter to Centimeter")
        print("\t30. Decimeter to Millimeter")
        print("\t31. Centimeter to Meter")
        print("\t32. Centimeter to Kilometer")
        print("\t33. Centimeter to Hectometer")
        print("\t34. Centimeter to Decameter")
        print("\t35. Centimeter to Decimeter")
        print("\t36. Centimeter to Millimeter")
        print("\t37. Millimeter to Meter")
        print("\t38. Millimeter to Kilometer")
        print("\t39. Millimeter to Hectometer")
        print("\t40. Millimeter to Decameter")
        print("\t41. Millimeter to Decimeter")
        print("\t42. Millimeter to Centimeter")

        choice = input("➡️ Choose a conversion (1-42), or 'exit' to quit: ")

        if choice == 'exit':
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            value = float(input("Enter value in Kilometer: "))
            if choice == '1':
                print(f"{value} kilometers is {kilometer_to_meter(value)} meters.")
            elif choice == '2':
                print(f"{value} kilometers is {kilometer_to_hectometer(value)} hectometers.")
            elif choice == '3':
                print(f"{value} kilometers is {kilometer_to_decameter(value)} decameters.")
            elif choice == '4':
                print(f"{value} kilometers is {kilometer_to_decimeter(value)} decimeters.")
            elif choice == '5':
                print(f"{value} kilometers is {kilometer_to_centimeter(value)} centimeters.")
            elif choice == '6':
                print(f"{value} kilometers is {kilometer_to_millimeter(value)} millimeters.")

        elif choice in ['7', '8', '9', '10', '11', '12']:
            value = float(input("Enter value in Hectometer: "))
            if choice == '7':
                print(f"{value} hectometers is {hectometer_to_kilometer(value)} kilometers.")
            elif choice == '8':
                print(f"{value} hectometers is {hectometer_to_meter(value)} meters.")
            elif choice == '9':
                print(f"{value} hectometers is {hectometer_to_decameter(value)} decameters.")
            elif choice == '10':
                print(f"{value} hectometers is {hectometer_to_decimeter(value)} decimeters.")
            elif choice == '11':
                print(f"{value} hectometers is {hectometer_to_centimeter(value)} centimeters.")
            elif choice == '12':
                print(f"{value} hectometers is {hectometer_to_millimeter(value)} millimeters.")

        elif choice in ['13', '14', '15', '16', '17', '18']:
            value = float(input("Enter value in Decameter: "))
            if choice == '13':
                print(f"{value} decameters is {decameter_to_kilometer(value)} kilometers.")
            elif choice == '14':
                print(f"{value} decameters is {decameter_to_hectometer(value)} hectometers.")
            elif choice == '15':
                print(f"{value} decameters is {decameter_to_meter(value)} meters.")
            elif choice == '16':
                print(f"{value} decameters is {decameter_to_decimeter(value)} decimeters.")
            elif choice == '17':
                print(f"{value} decameters is {decameter_to_centimeter(value)} centimeters.")
            elif choice == '18':
                print(f"{value} decameters is {decameter_to_millimeter(value)} millimeters.")

        # Handle other options (meter, decimeter, centimeter, millimeter) similarly. :<<<<

        else:
            print("\n⚠️ Invalid choice! Please choose a valid option.")
