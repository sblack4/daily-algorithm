"""
gets user input
determines if input is a palindrome
then returns true or false 
"""

def get_string():
    return input('Enter a string: \n ')

def is_palindrome(string):
    half_string_length = round(len(string)/2)
    for i in range(0, half_string_length):
        print("i " + str(i) + string[i] + " != " + string[-i-1])
        if string[i] != string[-i-1]:
           return False;
    return True; 

def main(script):
    input = get_string()
    input_palindrome = is_palindrome(input)
    print(input_palindrome)

if __name__ == '__main__':
    import sys
    main(*sys.argv)