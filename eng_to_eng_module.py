# Lengths
def yard_to_inch(num):
    return num * 36

def yard_to_foot(num):
    return num * 3

def yard_to_mile(num):
    return num / 1760

def inch_to_foot(num):
    return num / 12

def inch_to_yard(num):
    return num / 36

def inch_to_mile(num):
    return num / 63360

def foot_to_inch(num):
    return num * 12

def foot_to_yard(num):
    return num * 3

def foot_to_mile(num):
    return num / 5280

def mile_to_inch(num):
    return num * 63360

def mile_to_foot(num):
    return num * 5280

def mile_to_yard(num):
    return num * 1760


# Mass

def ounce_to_milligram(num):
    return num * 28349.5

def ounce_to_gram(num):
    return num * 28.3495

def ounce_to_kilogram(num):
    return num * 0.0283945

def milligram_to_gram(num):
    return num * 0.001

def milligram_to_ounce(num):
    return num / 28349.5

def milligram_to_kilogram(num):
    return num / 0.000001

def gram_to_milligram(num):
    return num * 0.0001

def gram_to_ounce(num):
    return num / 28.3495

def gram_to_kilogram(num):
    return num / 1000

def kilogram_to_milligram(num):
    return num * 0.000001

def kilogram_to_ounce(num):
    return num * 35.274

def kilogram_to_gram(num):
    return num * 1000

def gallons_to_liters(gallons):
    return gallons * 3.78541


def display_menu():
    while True:
        print("\n📏 Length Conversion Menu 📏")
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

        print("\n⚖️ Mass Conversion Menu ⚖️")
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

        choice = input("➡️ Choose a conversion (1-24) or type 'exit' to quit: ")
        if choice == 'exit':
            print("Goodbye!")
            break

        if choice == '1':
            value = float(input("Enter value in Yard: "))
            print(f"{value} Yard is {yard_to_inch(value)} Inch.")
        elif choice == '2':
            value = float(input("Enter value in Yard: "))
            print(f"{value} Yard is {yard_to_foot(value)} Foot.")
        elif choice == '3':
            value = float(input("Enter value in Yard: "))
            print(f"{value} Yard is {yard_to_mile(value)} Mile.")
        elif choice == '4':
            value = float(input("Enter value in Inch: "))
            print(f"{value} Inch is {inch_to_foot(value)} Foot.")
        elif choice == '5':
            value = float(input("Enter value in Inch: "))
            print(f"{value} Inch is {inch_to_yard(value)} Yard.")
        elif choice == '6':
            value = float(input("Enter value in Inch: "))
            print(f"{value} Inch is {inch_to_mile(value)} Mile.")
        elif choice == '7':
            value = float(input("Enter value in Foot: "))
            print(f"{value} Foot is {foot_to_inch(value)} Inch.")
        elif choice == '8':
            value = float(input("Enter value in Foot: "))
            print(f"{value} Foot is {foot_to_yard(value)} Yard.")
        elif choice == '9':
            value = float(input("Enter value in Foot: "))
            print(f"{value} Foot is {foot_to_mile(value)} Mile.")
        elif choice == '10':
            value = float(input("Enter value in Mile: "))
            print(f"{value} Mile is {mile_to_inch(value)} Inch.")
        elif choice == '11':
            value = float(input("Enter value in Mile: "))
            print(f"{value} Mile is {mile_to_foot(value)} Foot.")
        elif choice == '12':
            value = float(input("Enter value in Mile: "))
            print(f"{value} Mile is {mile_to_yard(value)} Yard.")

        elif choice == '13':
            value = float(input("Enter value in Ounce: "))
            print(f"{value} Ounce is {ounce_to_milligram(value)} Milligrams.")
        elif choice == '14':
            value = float(input("Enter value in Ounce: "))
            print(f"{value} Ounce is {ounce_to_gram(value)} Grams.")
        elif choice == '15':
            value = float(input("Enter value in Ounce: "))
            print(f"{value} Ounce is {ounce_to_kilogram(value)} Kilograms.")
        elif choice == '16':
            value = float(input("Enter value in Milligram: "))
            print(f"{value} Milligram is {milligram_to_gram(value)} Grams.")
        elif choice == '17':
            value = float(input("Enter value in Milligram: "))
            print(f"{value} Milligram is {milligram_to_ounce(value)} Ounces.")
        elif choice == '18':
            value = float(input("Enter value in Milligram: "))
            print(f"{value} Milligram is {milligram_to_kilogram(value)} Kilograms.")
        elif choice == '19':
            value = float(input("Enter value in Gram: "))
            print(f"{value} Gram is {gram_to_milligram(value)} Milligrams.")
        elif choice == '20':
            value = float(input("Enter value in Gram: "))
            print(f"{value} Gram is {gram_to_ounce(value)} Ounces.")
        elif choice == '21':
            value = float(input("Enter value in Gram: "))
            print(f"{value} Gram is {gram_to_kilogram(value)} Kilograms.")
        elif choice == '22':
            value = float(input("Enter value in Kilogram: "))
            print(f"{value} Kilogram is {kilogram_to_milligram(value)} Milligrams.")
        elif choice == '23':
            value = float(input("Enter value in Kilogram: "))
            print(f"{value} Kilogram is {kilogram_to_ounce(value)} Ounces.")
        elif choice == '24':
            value = float(input("Enter value in Kilogram: "))
            print(f"{value} Kilogram is {kilogram_to_gram(value)} Grams.")
        else:
            print("⚠️ Invalid choice. Please select a valid option.")
