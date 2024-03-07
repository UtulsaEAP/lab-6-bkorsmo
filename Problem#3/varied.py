def process_input(input_string):
      # Split into separate strings
    
    new = input_string.split(' ')
    

    # Convert strings to floats
    floatnew= list(map(float, new))




    

    # Get max and average
    max_value = max(floatnew)
    average_value = sum(floatnew)/ len(new)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
