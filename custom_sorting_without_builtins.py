#write a function that sorts a list from smallest to largesdt WITHOUT BUILT INS
#uses bubble or selection sort preferably


def custom_sort(numbers):
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    return sorted_numbers

#get input
user_input = input("Enter a list of numbers separated by commas: ")

#convert string to list of integers
numbers = [int(num.strip()) for num in user_input.split(',')]

#call the function
sorted_numbers = custom_sort(numbers)

print("sorted number list", sorted_numbers)