# Function to find the highest value of consonant substrings in a word
def solve(word):
    vowels = 'aeiou'
    max_value = 0
    current_value = 0

    # Iterating through each character in the word
    for char in word:
        # Checking if the character is a consonant
        if char not in vowels:
            # Calculating the value of the consonant and adding it to the current value
            current_value += ord(char) - ord('a') + 1
        else:
            # Updating the maximum value encountered so far
            max_value = max(max_value, current_value)
            # Resetting the current value for the next consonant substring
            current_value = 0

    # Returning the maximum value found among the consonant substrings
    return max(max_value, current_value)
