''' Name: Brady Korsmo
    Date: Thursday @2'''



def process_and_print(input_string): 
    tokens = input_string.split() 
    input_data = [int(token) for token in tokens if int(token) < 0]
    input_data.sort(reverse=True) 
    # Print sorted integers for value in input_data: 
    for value in input_data: 
        print(value, end=' ') 


if __name__ == "__main__": # User inputs string w/ numbers 
    user_input = input("Enter a space-separated string of numbers: ") # Call the function to process and print the result
    process_and_print(user_input)

    


