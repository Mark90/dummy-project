

def get_largest_number(values: list[int]) -> int:
    # Custom and slower implementation of 'max()'
    if not values:
        raise ValueError("List is empty")
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest
