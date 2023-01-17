import pytest as pytest

from reverse_5_digit_working_with_lists import reverse_digits


@pytest.mark.parametrize(
    'test_input, expected',
    [
        (12345, 54321),
        (123456, 165432),
        (1234567, 1276543),
        (36000, 63),
        (780000, 700008),
        (206578, 287560),
        (303030, 303030),
        (50709, 90705),
        (1234, 4321),
        (123, 321),
        (12, 21),
        (8, 8),
    ]
)
def test_reverse_digits(test_input, expected):
    assert reverse_digits(test_input) == expected
