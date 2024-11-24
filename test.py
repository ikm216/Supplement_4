import csv
import pytest

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
     """
    Given a list, converts list as a comma-delimited string.

    Args:
        list: The list getting converted to a string.

    Returns:
        Comma-delimited string.
    """
     return ",".join(list)

def write_csv(filename, headers, num):
    """
    Writes headers in function 2 and value in function 1 to a CSV file.

    Args:
        filename: The name of the CSV file.
        headers: A list of strings to convert to headers.
        num: The starting number for generating the value.

    Returns:
        Writes in the csv file
    """
    with open(filename, mode = 'w', newline='') as file:
        write = csv.writer(file)

        headers = convertTocds(headers).split(",")
        write.writerow(headers)

        row = next_10(num).split(",")
        write.writerow(row)

def test_should_return_next_ten_numbers():
    assert next_10(2) == "3,4,5,6,7,8,9,10,11,12"

def test_should_return_comma_delimited_string():
    assert convertTocds(["apple,bannana,orange"]) == "apple,bannana,orange"

def test_csv_writing(tmp_path):
    filename = tmp_path / "test_write.csv"

    headers = ["apple,bannana,orange"]
    num = 2

    write_csv(filename, headers, num)

    with open(filename, mode = 'r') as file:
        read = csv.reader(file)
        rows = list(read)

    test = convertTocds(headers).split(",")
    test2 = next_10(num).split(",")

    assert rows[0] == test
    assert rows[1] == test2