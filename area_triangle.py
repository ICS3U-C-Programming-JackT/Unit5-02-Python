#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 1st, 2025

# Area of triangle program

# Function to get, and print area
def area(height, base):
    area = height * base * 0.5
    print(area)

# Main function
def main():

    # Get height and base
    height = input("Please enter a height for your triangle: ")
    base = input("Please enter a base for your triangle: ")

    # Convert height and base to floats, if string, tell user
    try:
        height = float(height)
        try:
            base = float(base)
            # Check that both numbers are over 0
            if base > 0 and height > 0:
                area(height, base)
            else:
                print("Both numbers must be over 0")
        except:
            print("Error: please enter number values")
    except:
        print("Error: please enter number values")


if __name__ == "__main__":
    main()
