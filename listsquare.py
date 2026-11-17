def get_integer(p):
   
    while True:
        try:
            return int(input(p))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def square_and_separate(start, end):
   
    numbers = list(range(start, end + 1))
    squared_numbers = [n ** 2 for n in numbers]
    
    even_list = [n for n in squared_numbers if n % 2 == 0]
    odd_list = [n for n in squared_numbers if n % 2 != 0]
    
    return numbers, squared_numbers, even_list, odd_list

if __name__ == "__main__":
    
    start_num = get_integer("Enter starting number: ")
    end_num = get_integer("Enter ending number: ")
    
    # Ensure start <= end
    if start_num > end_num:
        start_num, end_num = end_num, start_num  # Swap if needed
    
    # Process numbers
    original, squared, evens, odds = square_and_separate(start_num, end_num)
    
    # Display results
    print(f"\nOriginal numbers: {original}")
    print(f"Squared numbers: {squared}")
    print(f"Even squared numbers: {evens}")
    print(f"Odd squared numbers: {odds}")

