"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]

def convert_weights(list_of_strings)

# if __name__ == "__main__":
    numbers_strings = ["1","2","4"]
    weight_strings = ["1","1","1"]        
    
    numbers = convert_numbers(numbers_strings)
    weights = convert_numbers(weight_strings)
    
    result = average_of_squares(numbers, weights)
    
    print(result)



import argparse ## import the library

if __name__ == "__main__":
    parser = argparse.ArgumentParser( ## given all numbers given in CLI after running python squares.py
        description="Calculate the sum of sqaures"
    )
    parser.add_argument(
        "numbers",
        nargs="+", # can simply be 1 for 1 number or we can use + for indefinite numbers in CLI
        help="Sequence of numbers to square and add",
        
    )

    parser.add_argument(
        "weights",
                nargs="+"
    )
    args = parser.parse_args() # read the defined inputs for above script

    

    numbers = convert_numbers(args.numbers)
    weights = convert_weights(args.numbers)

    result = average_of_squares(numbers, weights)
    print(result)


