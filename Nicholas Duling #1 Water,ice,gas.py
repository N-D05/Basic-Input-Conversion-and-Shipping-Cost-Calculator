# Problem 1
# User temp inputt
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert
celsius = (fahrenheit - 32) * 5 / 9

# Display temp cels
print("Temperature in Celsius:", round(celsius, 1))

# water form
if celsius <= 0:
    print("Ice")
elif celsius <= 100:
    print("Liquid")
else:
    print("Gas")