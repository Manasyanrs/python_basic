def expanding_nested_elements(file):
    result = []
    for element in file:
        if isinstance(element, int):
            result.append(element)
        else:
            result += expanding_nested_elements(element)
    return result


nice_digits = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
               [[11, 12, 13], [14, 15], [16, 17, 18]]]
