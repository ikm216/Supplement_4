def next_10(num):
    return ",".join(str(num + i) for i in range(1, 11))

def test_should_return_next_ten_numbers():
    assert next_10(2) == "3,4,5,6,7,8,9,10,11,12"
