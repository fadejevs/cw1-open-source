import main

def test_multiply_numbers():
    assert main.multiply_numbers(3, 5) == 15
    assert main.multiply_numbers(-1, 1) == -1


def test_devide_numbers():
    assert main.devide_numbers(3, 5) == 0.6
    assert main.devide_numbers(-1, 1) == -1
