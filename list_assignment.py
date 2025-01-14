# -*- coding: utf-8 -*-
"""List Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VFDU_Ofa250c5wckLWzYu4ICxtYpr377
"""

def alternate_elements():
    user_list = input("Enter the elements of the list separated by space: ").split()
    alternate_list = user_list[::2]
    print(f"Alternate elements of the list are: {alternate_list}")

# Example usage
alternate_elements()

def reverse_list():
    user_list = input("Enter the elements of the list separated by space: ").split()
    reversed_list = user_list[::-1]
    print(f"Reversed list: {reversed_list}")

# Example usage
reverse_list()

def largest_number():
    user_list = list(map(int, input("Enter the elements of the list separated by space: ").split()))
    largest = user_list[0]
    for num in user_list:
        if num > largest:
            largest = num
    print(f"The largest number in the list is: {largest}")

# Example usage
largest_number()

def rotate_list():
    user_list = input("Enter the elements of the list separated by space: ").split()
    rotated_list = user_list[1:] + user_list[:1]
    print(f"Rotated list: {rotated_list}")

# Example usage
rotate_list()

def delete_word():
    user_string = input("Enter a string: ")
    word_to_delete = input("Enter the word to delete: ")
    result_string = user_string.replace(word_to_delete, "")
    print(f"String after deleting the word: {result_string}")

# Example usage
delete_word()
