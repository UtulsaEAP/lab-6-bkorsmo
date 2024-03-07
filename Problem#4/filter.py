''' Name: Brady Korsmo
    Date: Thursday @2'''


def process_and_print(input_string):
      # Split into separate strings
    new = input_string.split()

    # Convert strings to integers and filter out negative values
    new1 = list(map(int, new))

    negatives = list(filter(lambda n: n<0, new1))
    # Sort integers in reverse order

    negatives.sort(reverse=True)




    
    # Print sorted integers

    print(' '.join(map(str, negatives)))
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
