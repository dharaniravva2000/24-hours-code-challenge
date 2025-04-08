# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:24:46 2025

@author: S24163336
"""

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_standard_deviation(numbers):
    mean = calculate_average(numbers)
    variance = 0
    for num in numbers:
        variance += (num - mean) ** 2
    variance /= len(numbers)
    
    # Manual square root calculation (using Newton's method)
    x = variance
    if x == 0:
        return 0
    guess = x / 2
    for _ in range(10):  # 10 iterations for better accuracy
        guess = (guess + x / guess) / 2
    return guess

def main():
    size = int(input("Enter the size of the population: "))
    if size <= 0:
        print("Invalid population")
        return
    
    numbers = []
    for i in range(size):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    mean = calculate_average(numbers)
    std_dev = calculate_standard_deviation(numbers)
    
    # Output as per requirement
    print(f"Average: {mean:.2f}")
    print(f"Population Standard Deviation: {std_dev:.2f}")

if __name__ == "__main__":
    main()