def is_multiple_of_three(num):
    """Return True if 'num' is a multiple of 3."""

    return num > 0 and num % 3 == 0


def filter_multiples_of_three(numbers):
    """Return all multiples of three in 'numbers' as a list."""

    return [n for n in numbers if is_multiple_of_three(n)]


if __name__ == "__main__":
    
    print(filter_multiples_of_three(range(87)))
