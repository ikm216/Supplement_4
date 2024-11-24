def next_10(num):
    """
    Given a number, gets the next 10 numbers as a comma-delimited string.

    Args:
        num: The starting number.

    Returns:
        Comma-delimited string of the next 10 numbers.
    """
    return ",".join(str(num + i) for i in range(1, 11))

def convertTocds(list):
    return ",".join(list)

def test_should_return_next_ten_numbers():
    assert next_10(2) == "3,4,5,6,7,8,9,10,11,12"

def test_should_return_comma_delimited_string():
    assert convertTocds(["apple,bannana,orange"]) == "apple,bannana,orange"
