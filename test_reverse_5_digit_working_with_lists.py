import pytest as pytest

from reverse_5_digit_working_with_lists import reverse_digits


@pytest.mark.parametrize(
    'test_input, expected',
    [
        (1234567, 1276543),
        (25000, 52),
    ]
)
def test_reverse_digits(test_input, expected):
    assert reverse_digits(test_input) == expected
