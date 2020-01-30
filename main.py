print("Welcome to the Temperature conversion app")

fahr = float(input("\nWhat is the given temp in degrees Fahrenheit: "))

cel = (5/9)*(fahr-32)
kel = cel + 273.15

fahr = round(fahr, 4)
cel = round(cel, 4)
kel = round(kel, 4)

print(f"\nDegrees Fahreneheit: {fahr} \nDegrees celcious:\t {cel} \nDegrees kelvin:\t\t {kel}")