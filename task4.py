def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        return "Provide positive integer"
    
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b

def main():
    n = input("Enter a positive integer for Fibonacci sequence: ")
    
    # Check if the input is a positive integer
    if n.isdigit():
        n = int(n)
        print(f"The {n}th Fibonacci number is {fibonacci(n)}")
    else:
        print("Provide positive integer")

if __name__ == "__main__":
    main()