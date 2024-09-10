def main():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    try:
        num1 = int(num1)
        num2 = int(num2)
        
        total = num1 + num2
        
        print(f"The sum of {num1} and {num2} is {total}.")
    
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()