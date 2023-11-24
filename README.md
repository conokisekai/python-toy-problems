# Phase 3 Week 1(Toy Problems)

## Description:

This repository contains Python solutions for three coding challenges aimed at practicing Python programming.


### Challenge 1: Converting 12-hour time to 24-hour time

Given a time in the 12-hour format ("8:30 am" or "8:30 pm"), this function converts it to the 24-hour format ("0830" or "2030").

#### Function:
- **convert_to_24_hour(hour, minute, period):**
  - Converts a time in the 12-hour format to a 24-hour format.
  - Parameters:
    - `hour`: Integer representing the hour (range: 1 to 12)
    - `minute`: Integer representing the minute (range: 0 to 59)
    - `period`: String representing either "am" or "pm"
  - Returns:
    - A four-digit string representing the time in 24-hour format (e.g., "0830" or "2030").

### Challenge 2: Two numbers are positive

Write a function that takes three integers as arguments and returns True if exactly two out of the three integers are positive.

#### Function:
- **two_positive(a, b, c):**
  - Checks if exactly two out of three integers are positive.
  - Parameters:
    - `a`, `b`, `c`: Integers to be evaluated.
  - Returns:
    - `True` if exactly two numbers are positive; `False` otherwise.

### Challenge 3: Consonant value

Given a lowercase string with alphabetic characters only and no spaces, this function returns the highest value of consonant substrings.

#### Function:
- **solve(word):**
  - Finds the highest value of consonant substrings in a given word.
  - Parameters:
    - `word`: A lowercase string containing alphabetic characters only (no spaces).
  - Returns:
    - The highest value of consonant substrings.

## Project Setup

1. Create a repository on your GitHub account.
2. Clone the repository to your local machine using `git clone`.
3. Use Python to implement the solutions.
   Each challenge has a corresponding Python file ( `convert_time.py`, `two_positive_numbers.py`, `consonant_value.py`).
4. Run the Python files using `python filename.py` in your terminal to test the solutions.
5. Push the solutions to the repository.
6. Submit the repository link for grading.
7. Ensure your repository has a well-written README.

## Author

Conrad Kambi
https://github.com/conokisekai

# LICENCE
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>