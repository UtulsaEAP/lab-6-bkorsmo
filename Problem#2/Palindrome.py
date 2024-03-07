''' Name: Brady Korsmo
    Date: Thursday @2'''


def check_palindrome(user_input):
 #type your code here
    checker = user_input[::-1]
    correct = user_input
    if checker == correct:
        print('palindrome: '+ checker)
    else:
        print('not a palindrome: '+ user_input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
