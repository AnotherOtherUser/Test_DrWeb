import pytest
import main


def test_even_fibonacci():
    even_num = 4
    assert main.even_fibonacci(even_num) == [0, 2, 8, 34]


if __name__ == '__main__':
    pytest.main()
