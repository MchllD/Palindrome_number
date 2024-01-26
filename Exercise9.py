# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# pseudocode

# Convert the number to a string to work with individual digits
# Reverse the given number
# Check if the number is a palindrome
# Example 1: Palindrome number
# Example 2: Non-palindrome number

# ____________________________________ actual code __________________________________


def check_palindrome_number(number):
    print("Original number:", number)
    original_num = number 
    
    
    # Convert the number to a string to work with individual digits
    num_str = str(number)
    
    
    # Reverse the given number
    reversed_num_str = num_str[::-1]
    
    
    # Check if the number is a palindrome
    if num_str == reversed_num_str:
        print("The given number is a palindrome.")
    else:
        print("The given number is not a palindrome.")

    
    
    