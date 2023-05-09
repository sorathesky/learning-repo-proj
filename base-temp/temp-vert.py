temp_scale = ""
temp = 0.0
while temp_scale != "q":
    # Select to convert from C to F or F to C
    temp_scale = input("Enter a temperature scale to convert from\n(C or F or q to exit): ")
    if temp_scale == "q":
        print("Exiting...")
        break
    else:
        # Ask for temperature value
        temp = float(input("Enter a temperature: \n"))

        # Convert from C to F or F to C
        if temp_scale == "C":
            print(temp * 9/5 + 32)
        elif temp_scale == "F":
            print((temp - 32) * 5/9)
        elif temp_scale == "q":
            print("Exiting...")
            break
        else:
            print("Invalid scale")
