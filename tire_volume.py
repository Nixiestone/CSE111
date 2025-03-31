# Exceeded requirements by adding a purchase inquiry feature: asks the user if they want to buy tires and stores their phone number if they say yes.
import math
from datetime import datetime

def main():
    """Calculates and prints the approximate volume of a tire and stores data."""
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume:.2f} liters")

    buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
    phone_number = ""
    if buy_tires == "yes":
        phone_number = input("Enter your phone number: ")

    store_tire_data(width, aspect_ratio, diameter, volume, phone_number)

def calculate_tire_volume(width, aspect_ratio, diameter):
    """Calculates the approximate volume of a tire."""
    w = width
    a = aspect_ratio
    d = diameter

    # Formula to calculate tire volume in liters
    v = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000
    return v

def store_tire_data(width, aspect_ratio, diameter, volume, phone_number=""):
    """Stores tire data in a text file."""
    current_date = datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")

    # Open the file in append mode and write the data
    with open("volumes.txt", "at") as volumes_file:
        volumes_file.write(f"{date_string}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}\n")

if __name__ == "__main__":
    main()