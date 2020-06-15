"""
Some module docstring
"""

import pytest


def capital_case(string):
    """
    This method capitalizes string
    :param string: string to capitalize
    :return: capitalized string
    """
    return string.capitalize()


def test_capital_case():
    """
    Test if string is correctly capitalized
    """
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    """
    Test if there is exception when non string argument passed
    """
    with pytest.raises(AttributeError):
        capital_case(9)
