# Function to check if exactly two out of three numbers are positive
def two_positive(a, b, c):
    nums = [a, b, c]
    # Counting the number of positive integers using list comprehension
    positive_count = sum(num > 0 for num in nums)
    # Checking if exactly two numbers are positive
    return positive_count == 2
