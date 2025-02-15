import temp_to_temp_module
import english_to_metric_module
import eng_to_eng_module
import met_to_eng_module
from met_to_met_module import (kilometer_to_meter, kilometer_to_hectometer, kilometer_to_decameter,
    kilometer_to_decimeter, kilometer_to_centimeter, kilometer_to_millimeter, hectometer_to_kilometer,
    hectometer_to_meter, hectometer_to_decameter, hectometer_to_decimeter, hectometer_to_centimeter,
    hectometer_to_millimeter, decameter_to_kilometer, decameter_to_hectometer, decameter_to_meter,
    decameter_to_decimeter, decameter_to_centimeter, decameter_to_millimeter, meter_to_kilometer, meter_to_hectometer,
    meter_to_decameter, meter_to_decimeter, meter_to_centimeter, meter_to_millimeter, decimeter_to_meter,
    decimeter_to_kilometer, decimeter_to_hectometer, decimeter_to_decameter, decimeter_to_centimeter,
    decimeter_to_millimeter, centimeter_to_meter, centimeter_to_kilometer, centimeter_to_hectometer,
    centimeter_to_decameter, centimeter_to_decimeter, centimeter_to_millimeter, millimeter_to_meter,
    millimeter_to_kilometer, millimeter_to_hectometer, millimeter_to_decameter, millimeter_to_decimeter,
    millimeter_to_centimeter)


def display_main_menu():
    print("\n🌟 Welcome to Conversion Calculator! 🌟")
    print("\t➡️ What would you like to convert?")
    print("\t\t1. English to Metric")
    print("\t\t2. Metric to English")
    print("\t\t3. English to English")
    print("\t\t4. Metric to Metric")
    print("\t\t5. Temperature")
    print("\t\tType 'stop' to exit.")


def get_input(prompt):
    inp = input(f"{prompt} (or type 'back' to return, 'stop' to exit): ").lower()
    if inp == "stop":
        print("\n🚀 Program stopped. Goodbye!\n")
        exit()
    if inp == "back":
        return "back"
    try:
        return float(inp)
    except ValueError:
        print("Invalid input, please enter a number, 'back', or 'stop'.")
        return get_input(prompt)


def english_to_metric_menu():
    while True:
        print("\n📏 English to Metric Conversions 📏")
        print("\t1. Inches to Centimeters")
        print("\t2. Feet to Centimeters")
        print("\t3. Yards to Meters")
        print("\t4. Feet to Meters")
        print("\t5. Miles to Kilometers")
        print("\t6. Ounces to Grams")
        print("\t7. Pounds to Kilograms")
        print("\t8. Gallons to Liters")
        print("\t9. Quarts to Liters")
        print("\t10. Pints to Liters")
        print("\t11. Cups to Milliliters")
        print("\t12. Square Inches to Square Centimeters")
        print("\t13. Square Feet to Square Meters")
        print("\t14. Acres to Hectares")
        print("\tType 'back' to return to the main menu.")
        choice = input("➡️ Choose a conversion (1-14): ").lower()
        if choice == "back":
            break
        try:
            val = get_input("Enter value")
            if val == "back": continue
            if choice == '1':
                print(f"{val} inches is {english_to_metric_module.inch_to_cm(val)} centimeters.")
            elif choice == '2':
                print(f"{val} feet is {english_to_metric_module.foot_to_cm(val)} centimeters.")
            elif choice == '3':
                print(f"{val} yards is {english_to_metric_module.yard_to_meter(val)} meters.")
            elif choice == '4':
                print(f"{val} feet is {english_to_metric_module.foot_to_meter(val)} meters.")
            elif choice == '5':
                print(f"{val} miles is {english_to_metric_module.miles_to_kilometer(val)} kilometers.")
            elif choice == '6':
                print(f"{val} ounces is {english_to_metric_module.ounce_to_grams(val)} grams.")
            elif choice == '7':
                print(f"{val} pounds is {english_to_metric_module.pound_to_kilogram(val)} kilograms.")
            elif choice == '8':
                print(f"{val} gallons is {english_to_metric_module.gallon_to_liter(val)} liters.")
            elif choice == '9':
                print(f"{val} quarts is {english_to_metric_module.quart_to_liter(val)} liters.")
            elif choice == '10':
                print(f"{val} pints is {english_to_metric_module.pint_to_liter(val)} liters.")
            elif choice == '11':
                print(f"{val} cups is {english_to_metric_module.cup_to_milliliter(val)} milliliters.")
            elif choice == '12':
                print(f"{val} square inches is {english_to_metric_module.square_inch_to_square_cm(val)} square centimeters.")
            elif choice == '13':
                print(f"{val} square feet is {english_to_metric_module.square_foot_to_square_meter(val)} square meters.")
            elif choice == '14':
                print(f"{val} acres is {english_to_metric_module.acre_to_hectare(val)} hectares.")
            else:
                print("Invalid choice. Please choose from 1-14 or 'back'.")
        except Exception as e:
            print("Error during conversion:", e)


def metric_to_english_menu():
    while True:
        print("\n📏 Metric to English Conversions 📏")
        print("\t1. Centimeters to Inches")
        print("\t2. Centimeters to Feet")
        print("\t3. Centimeters to Yards")
        print("\t4. Centimeters to Miles")
        print("\t5. Millimeters to Inches")
        print("\t6. Millimeters to Feet")
        print("\t7. Millimeters to Yards")
        print("\t8. Millimeters to Miles")
        print("\t9. Meters to Inches")
        print("\t10. Meters to Feet")
        print("\t11. Meters to Yards")
        print("\t12. Meters to Miles")
        print("\t13. Kilometers to Inches")
        print("\t14. Kilometers to Feet")
        print("\t15. Kilometers to Yards")
        print("\t16. Kilometers to Miles")
        print("\t17. Kilograms to Pounds")
        print("\t18. Kilograms to Ounces")
        print("\t19. Grams to Ounces")
        print("\t20. Grams to Pounds")
        print("\t21. Liters to Gallons")
        print("\t22. Liters to Ounces")
        print("\t23. Liters to Quarts")
        print("\t24. Liters to Pints")
        print("\t25. Liters to Cups")
        print("\t26. Milliliters to Ounces")
        print("\t27. Milliliters to Gallons")
        print("\t28. Milliliters to Quarts")
        print("\t29. Milliliters to Pints")
        print("\t30. Milliliters to Cups")
        print("\t31. Square Meters to Square Feet")
        print("\t32. Hectares to Acres")
        print("\t33. Square Kilometers to Square Miles")
        print("\tType 'back' to return to the main menu.")
        choice = input("➡️ Choose a conversion (1-33): ").lower()
        if choice == "back":
            break
        try:
            val = get_input("Enter value")
            if val == "back": continue
            func_list = list(met_to_eng_module.__dict__.values())
            func_keys = list(met_to_eng_module.__dict__.keys())
            if 1 <= int(choice) <= len(func_keys):
                result = func_list[int(choice) - 1](val)
                print(f"{val} converted is {result}.")
            else:
                print("Invalid choice. Please choose from 1-33 or 'back'.")
        except Exception as e:
            print("Error during conversion:", e)


def eng_to_eng_menu():
    while True:
        print("\n🔢 English to English Conversions 🔢")
        print("\t1. Yard to Inch")
        print("\t2. Yard to Foot")
        print("\t3. Yard to Mile")
        print("\t4. Inch to Foot")
        print("\t5. Inch to Yard")
        print("\t6. Inch to Mile")
        print("\t7. Foot to Inch")
        print("\t8. Foot to Yard")
        print("\t9. Foot to Mile")
        print("\t10. Mile to Inch")
        print("\t11. Mile to Foot")
        print("\t12. Mile to Yard")
        print("\t13. Ounce to Milligram")
        print("\t14. Ounce to Gram")
        print("\t15. Ounce to Kilogram")
        print("\t16. Milligram to Gram")
        print("\t17. Milligram to Ounce")
        print("\t18. Milligram to Kilogram")
        print("\t19. Gram to Milligram")
        print("\t20. Gram to Ounce")
        print("\t21. Gram to Kilogram")
        print("\t22. Kilogram to Milligram")
        print("\t23. Kilogram to Ounce")
        print("\t24. Kilogram to Gram")
        print("\tType 'back' to return to the main menu.")
        choice = input("➡️ Choose a conversion (1-24): ").lower()
        if choice == "back":
            break
        try:
            val = get_input("Enter value")
            if val == "back": continue
            func_list = list(eng_to_eng_module.__dict__.values())
            func_keys = list(eng_to_eng_module.__dict__.keys())
            if 1 <= int(choice) <= len(func_keys):
                result = func_list[int(choice) - 1](val)
                print(f"{val} converted is {result}.")
            else:
                print("Invalid choice. Please choose from 1-24 or 'back'.")
        except Exception as e:
            print("Error during conversion:", e)


def metric_to_metric_menu():
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
        print("\tType 'back' to return to the main menu.")
        choice = input("➡️ Choose a conversion (1-42): ").lower()
        if choice == "back":
            break
        try:
            val = get_input("Enter value to convert")
            if val == "back": continue
            if choice == '1':
                result = kilometer_to_meter(val)
                print(f"{val} kilometers is {result} meters.")
            elif choice == '2':
                result = kilometer_to_hectometer(val)
                print(f"{val} kilometers is {result} hectometers.")
            elif choice == '3':
                result = kilometer_to_decameter(val)
                print(f"{val} kilometers is {result} decameters.")
            elif choice == '4':
                result = kilometer_to_decimeter(val)
                print(f"{val} kilometers is {result} decimeters.")
            elif choice == '5':
                result = kilometer_to_centimeter(val)
                print(f"{val} kilometers is {result} centimeters.")
            elif choice == '6':
                result = kilometer_to_millimeter(val)
                print(f"{val} kilometers is {result} millimeters.")
            elif choice == '7':
                result = hectometer_to_kilometer(val)
                print(f"{val} hectometers is {result} kilometers.")
            elif choice == '8':
                result = hectometer_to_meter(val)
                print(f"{val} hectometers is {result} meters.")
            elif choice == '9':
                result = hectometer_to_decameter(val)
                print(f"{val} hectometers is {result} decameters.")
            elif choice == '10':
                result = hectometer_to_decimeter(val)
                print(f"{val} hectometers is {result} decimeters.")
            elif choice == '11':
                result = hectometer_to_centimeter(val)
                print(f"{val} hectometers is {result} centimeters.")
            elif choice == '12':
                result = hectometer_to_millimeter(val)
                print(f"{val} hectometers is {result} millimeters.")
            elif choice == '13':
                result = decameter_to_kilometer(val)
                print(f"{val} decameters is {result} kilometers.")
            elif choice == '14':
                result = decameter_to_hectometer(val)
                print(f"{val} decameters is {result} hectometers.")
            elif choice == '15':
                result = decameter_to_meter(val)
                print(f"{val} decameters is {result} meters.")
            elif choice == '16':
                result = decameter_to_decimeter(val)
                print(f"{val} decameters is {result} decimeters.")
            elif choice == '17':
                result = decameter_to_centimeter(val)
                print(f"{val} decameters is {result} centimeters.")
            elif choice == '18':
                result = decameter_to_millimeter(val)
                print(f"{val} decameters is {result} millimeters.")
            elif choice == '19':
                result = meter_to_kilometer(val)
                print(f"{val} meters is {result} kilometers.")
            elif choice == '20':
                result = meter_to_hectometer(val)
                print(f"{val} meters is {result} hectometers.")
            elif choice == '21':
                result = meter_to_decameter(val)
                print(f"{val} meters is {result} decameters.")
            elif choice == '22':
                result = meter_to_decimeter(val)
                print(f"{val} meters is {result} decimeters.")
            elif choice == '23':
                result = meter_to_centimeter(val)
                print(f"{val} meters is {result} centimeters.")
            elif choice == '24':
                result = meter_to_millimeter(val)
                print(f"{val} meters is {result} millimeters.")
            elif choice == '25':
                result = decimeter_to_meter(val)
                print(f"{val} decimeters is {result} meters.")
            elif choice == '26':
                result = decimeter_to_kilometer(val)
                print(f"{val} decimeters is {result} kilometers.")
            elif choice == '27':
                result = decimeter_to_hectometer(val)
                print(f"{val} decimeters is {result} hectometers.")
            elif choice == '28':
                result = decimeter_to_decameter(val)
                print(f"{val} decimeters is {result} decameters.")
            elif choice == '29':
                result = decimeter_to_centimeter(val)
                print(f"{val} decimeters is {result} centimeters.")
            elif choice == '30':
                result = decimeter_to_millimeter(val)
                print(f"{val} decimeters is {result} millimeters.")
            elif choice == '31':
                result = centimeter_to_meter(val)
                print(f"{val} centimeters is {result} meters.")
            elif choice == '32':
                result = centimeter_to_kilometer(val)
                print(f"{val} centimeters is {result} kilometers.")
            elif choice == '33':
                result = centimeter_to_hectometer(val)
                print(f"{val} centimeters is {result} hectometers.")
            elif choice == '34':
                result = centimeter_to_decameter(val)
                print(f"{val} centimeters is {result} decameters.")
            elif choice == '35':
                result = centimeter_to_decimeter(val)
                print(f"{val} centimeters is {result} decimeters.")
            elif choice == '36':
                result = centimeter_to_millimeter(val)
                print(f"{val} centimeters is {result} millimeters.")
            elif choice == '37':
                result = millimeter_to_meter(val)
                print(f"{val} millimeters is {result} meters.")
            elif choice == '38':
                result = millimeter_to_kilometer(val)
                print(f"{val} millimeters is {result} kilometers.")
            elif choice == '39':
                result = millimeter_to_hectometer(val)
                print(f"{val} millimeters is {result} hectometers.")
            elif choice == '40':
                result = millimeter_to_decameter(val)
                print(f"{val} millimeters is {result} decameters.")
            elif choice == '41':
                result = millimeter_to_decimeter(val)
                print(f"{val} millimeters is {result} decimeters.")
            elif choice == '42':
                result = millimeter_to_centimeter(val)
                print(f"{val} millimeters is {result} centimeters.")
            else:
                print("Invalid choice. Please choose from 1-42 or 'back'.")
        except Exception as e:
            print("Error during conversion:", e)


def temperature_menu():
    while True:
        print("\n🌡️ Temperature Conversions 🌡️")
        print("\t1. Celsius to Fahrenheit")
        print("\t2. Fahrenheit to Celsius")
        print("\t3. Celsius to Kelvin")
        print("\t4. Kelvin to Celsius")
        print("\t5. Fahrenheit to Kelvin")
        print("\t6. Kelvin to Fahrenheit")
        print("\tType 'back' to return to the main menu.")
        choice = input("➡️ Choose a conversion (1-6): ").lower()
        if choice == "back":
            break
        try:
            if choice == '1':
                val = get_input("Enter value in Celsius")
                if val == "back": continue
                result = temp_to_temp_module.celsius_to_fahrenheit(val)
                print(f"{val} °C is {result} °F.")
            elif choice == '2':
                val = get_input("Enter value in Fahrenheit")
                if val == "back": continue
                result = temp_to_temp_module.fahrenheit_to_celsius(val)
                print(f"{val} °F is {result} °C.")
            elif choice == '3':
                val = get_input("Enter value in Celsius")
                if val == "back": continue
                result = temp_to_temp_module.celsius_to_kelvin(val)
                print(f"{val} °C is {result} K.")
            elif choice == '4':
                val = get_input("Enter value in Kelvin")
                if val == "back": continue
                result = temp_to_temp_module.kelvin_to_celsius(val)
                print(f"{val} K is {result} °C.")
            elif choice == '5':
                val = get_input("Enter value in Fahrenheit")
                if val == "back": continue
                result = temp_to_temp_module.fahrenheit_to_kelvin(val)
                print(f"{val} °F is {result} K.")
            elif choice == '6':
                val = get_input("Enter value in Kelvin")
                if val == "back": continue
                result = temp_to_temp_module.kelvin_to_fahrenheit(val)
                print(f"{val} K is {result} °F.")
            else:
                print("Invalid choice. Please choose from 1-6 or 'back'.")
        except Exception as e:
            print("Error during conversion:", e)


def main():
    while True:
        display_main_menu()
        choice = input("➡️ Please choose an option (1-5): ").lower()
        if choice == "1":
            english_to_metric_menu()
        elif choice == "2":
            metric_to_english_menu()
        elif choice == "3":
            eng_to_eng_menu()
        elif choice == "4":
            metric_to_metric_menu()
        elif choice == "5":
            temperature_menu()
        else:
            print("Invalid option. Please select a valid option or type 'stop' to exit.")


if __name__ == "__main__":
    main()
