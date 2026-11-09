from patterns import repeated_chars
import pytest

class TestRepeatedChars:
      
  def test_no_repetitions(self):
    result = repeated_chars("abc")
    assert result == []

  def test_invalid_password_type(self):
    with pytest.raises(TypeError):
      repeated_chars(12345)

  def test_invalid_repetitions_type(self):
    with pytest.raises(TypeError):
      repeated_chars("abc", "abc")

  def test_invalid_repetitions_value(self):
    with pytest.raises(ValueError):
      repeated_chars("abc", 0)

  def test_returns_empty_list_if_password_is_empty(self):
    password = ""
    assert repeated_chars(password) == []

  def test_works_under_normal_circumstances(self):
    password = "aaaBBc"
    assert repeated_chars(password) == [
      {'type': 'repeated_char', 'value': 'aaa', 'start': 0, 'end': 3, 'length': 3}, 
      {'type': 'repeated_char', 'value': 'BB', 'start': 3, 'end': 5, 'length': 2}
      ]
  def test_returns_nothing_if_there_is_no_repetition(self):
    password = "abcd"
    assert repeated_chars(password) == []

  def test_respects_min_repetitions_amount(self):
    password = "aaaBBcDd"
    assert repeated_chars(password, 3) == [
      {'type': 'repeated_char', 'value': 'aaa', 'start': 0, 'end': 3, 'length': 3}
    ]  

  def test_works_with_number_repetition(self):
    password = "111Aavb"
    assert repeated_chars(password) == [
      {'type': 'repeated_char', 'value': '111', 'start': 0, 'end': 3, 'length': 3}
    ]

  def test_works_when_group_at_end(self):
    password = "abcdddd"
    assert repeated_chars(password) == [
      {'type': 'repeated_char', 'value': 'dddd', 'start': 3, 'end': 7, 'length': 4}
    ]

  def test_returns_nothing_when_only_one_char(self):
    password = "a"
    assert repeated_chars(password) == []

  def test_works_when_the_password_is_the_group(self):
    password = "aaa"
    assert repeated_chars(password) == [
      {'type': 'repeated_char', 'value': 'aaa', 'start': 0, 'end': 3, 'length': 3}
    ]

  def test_raises_error_when_repetitions_is_bool(self):
    with pytest.raises(TypeError):
      repeated_chars("adawa", True)

  def test_works_with_special_chars(self):
    password = "ăă😊😊"
    assert repeated_chars(password) == [
      {'type': 'repeated_char', 'value': 'ăă', 'start': 0, 'end': 2, 'length': 2},
      {'type': 'repeated_char', 'value': '😊😊', 'start': 2, 'end': 4, 'length': 2},
    ]