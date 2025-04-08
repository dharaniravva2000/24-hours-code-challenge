# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:44:48 2025

@author: S24163336
"""

def get_house_data():
    houses = []
    for i in range(7):
        while True:
            try:
                count = int(input(f"Provide the number of houses with {i} occupancy: "))
                if count < 0:
                    print("Program should ask to input vaild house number")
                    continue
                houses.append(count)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            count = int(input(f"Provide the number of houses with occupancy > 6: "))
            if count < 0:
                print("Program should ask to input vaild house number")
                continue
            houses.append(count)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return houses

def calculate_percentage(value, total):
    if total == 0:
        return 0
    return (value / total) * 100

def main():
    houses = get_house_data()
    total = sum(houses)

    print("\nOccupants            0       1       2       3       4       5       6      >6")
    print("No. dwellings    ", end="")
    for h in houses:
        print(f"{h:<8}", end="")
    print("\nPercentage        ", end="")
    for h in houses:
        print(f"{calculate_percentage(h, total):.1f}%  ", end="")
    print()

if __name__ == "__main__":
    main()