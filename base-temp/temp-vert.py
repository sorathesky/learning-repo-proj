temp_scale = ""

def converter(temp_scale, temp):
    if temp_scale == "C":
        return temp * 9/5 + 32
    elif temp_scale == "F":
        return (temp - 32) * 5/9
    elif temp_scale == "q":
        return "Exiting..."
    else:
        return "Invalid scale"

while temp_scale != "q":
    # Select to convert from C to F or F to C
    temp_scale = input("Enter a temperature scale to convert from\n(C or F or q to exit): ")

    # Ask for temperature value
    temp = float(input("Enter a temperature: \n"))

    # Convert from C to F
    print(converter(temp_scale, temp))