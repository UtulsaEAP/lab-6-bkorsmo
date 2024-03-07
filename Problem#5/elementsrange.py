''' Name: Brady Korsmo
    Date: Thursday @2'''


def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    

    # Get the lower and upper bounds
    lower_bound, upper_bound = min_val, max_val

    # Output integers within the specified range
    for num in input_list:
        if lower_bound <= num <= upper_bound:
            print(num, end=',')

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integers = list(map(int, user_input.split()))

    # Get input for the range (min and max values)
    user_input1 = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, user_input1.split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integers, min_val, max_val)
   
