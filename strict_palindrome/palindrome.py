"""
gets user input
determines if input is a palindrome
then returns true or false
"""

def get_string():
    """ get user input"""
    return input('Enter a string: \n ')

def is_palindrome(string):
    """determines if input string is palindrom, returns bool"""
    half_string_length = round(len(string)/2)
    for i in range(0, half_string_length):
        # print("i " + str(i) + string[i] + " != " + string[-i-1])
        if string[i] != string[-i-1]:
            return False
    return True

def main():
    """main function """
    input_str = get_string()
    input_palindrome = is_palindrome(input_str)
    print(input_str + " is a palindrome: " + str(input_palindrome))

if __name__ == '__main__':
    # import sys
    main()
