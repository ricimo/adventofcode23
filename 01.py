# Initialize a variable to hold the total
total = 0

# Open the file for reading
with open("input01.txt", "r") as file:
    # Go through each line in the file
    for line in file:
        # Get all the digits in the line
        digits = [char for char in line if char.isdigit()]
            # Form a new number from the first and last digit
        number = int(digits[0] + digits[-1])

            # Add the number to the total
        total += number

# Print the total
print("The total is:", total)
