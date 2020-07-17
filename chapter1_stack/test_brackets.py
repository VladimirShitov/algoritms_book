import pytest

from chapter1_stack.brackets import is_bracket_sequence_valid


def test_valid_sequence():
    assert is_bracket_sequence_valid("(){[](){}}")


def test_invalid_sequence():
    assert not is_bracket_sequence_valid("{)")


def test_only_opening_brackets():
    assert not is_bracket_sequence_valid("[[[[[((({{{")


def test_only_closing_brackets():
    assert not is_bracket_sequence_valid("}}}}]]])))")


def test_wrong_symbols():
    with pytest.raises(ValueError):
        is_bracket_sequence_valid("{_}")


def test_empty_string():
    assert is_bracket_sequence_valid("")