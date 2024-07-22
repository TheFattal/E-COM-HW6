import  random

# a:
numbers_list = [random.randint(1000, 9999) for _ in range(10)]
# b:
# Initialize an empty list to store numbers
numbers = []

while True:
    try:
        # Receive input from the user
        num_str = input("Enter a number (-999 to exit): ")

        # Convert input to integer
        num = int(num_str)

        # Check if the user wants to exit
        if num == -999:
            break

        # Add number to the list
        numbers.append(num)

        # Print the element at the corresponding index
        print(f"Element at index {len(numbers) - 1}: {numbers[-1]}")

    except ValueError:
        print(f"Error: '{num_str}' is not a valid number.")
    except IndexError:
        print(f"Error: Index '{len(numbers) - 1}' is out of range for the current list.")
