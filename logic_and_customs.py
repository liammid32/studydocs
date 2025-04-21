# goal is write a function that accepts list of integers and returns a list of even numbers
def get_even_nums(numbers):
    """
    Filters even numbers from a list of integers.

    Args:
        numbers: a list of integers.

    Returns:
        A new list containing only the even numbers from the list inputted.
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers  

#number usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_nums(numbers)
print(even_numbers) #output should be 2, 4, 6 , 8, 10