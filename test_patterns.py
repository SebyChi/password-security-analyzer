from patterns import repeated_chars, get_sequence_direction, same_category, detect_sequences, detect_repeated_substrings, is_redundant_pattern
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

class TestSeqDirection:

  def test_invalid_when_char1_is_not_a_str(self):
    with pytest.raises(TypeError):
      get_sequence_direction(1, "a")

  def test_invalid_when_char2_is_not_a_str(self):
    with pytest.raises(TypeError):
      get_sequence_direction("1", 2)

  def test_invalid_when_char1_is_empty(self):
    with pytest.raises(ValueError):
      get_sequence_direction("", "2")

  def test_invalid_when_char2_is_empty(self):
    with pytest.raises(ValueError):
      get_sequence_direction("1", "")
      
  def test_invalid_when_char1_is_invalid(self):
    with pytest.raises(ValueError):
      get_sequence_direction("ab", "a")

  def test_invalid_when_char2_is_invalid(self):
    with pytest.raises(ValueError):
      get_sequence_direction("a", "ab")

  def test_returns_1_when_seq_is_ascending(self):
    assert get_sequence_direction("a", "b") == 1

  def test_returns_1_when_seq_is_ascending_case_insensitive(self):
    assert get_sequence_direction("a", "B") == 1

  def test_returns_1_when_seq_is_ascending_numbers(self):
    assert get_sequence_direction("1", "2") == 1

  def test_returns_negative_1_when_seq_is_descending(self):
    assert get_sequence_direction("b", "a") == -1

  def test_returns_negative_1_when_seq_is_descending_case_insensitive(self):
    assert get_sequence_direction("B", "a") == -1

  def test_returns_negative_1_when_seq_is_descending_numbers(self):
    assert get_sequence_direction("2", "1") == -1

  def test_returns_0_when_there_is_no_order(self):
    assert get_sequence_direction("a", "C") == 0

  def test_returns_0_if_ordered_but_not_from_same_category(self):
    assert get_sequence_direction("9", ":") == 0

  def test_does_not_allow_restart_of_alphabet(self):
    assert get_sequence_direction("z", "a") == 0

  def test_does_not_include_outside_ASCII_chars(self):
    assert get_sequence_direction("é", "ê") == 0

  def test_does_not_include_same_chars(self):
    assert get_sequence_direction("a", "A") == 0

class TestSameCategory:
  def test_returns_true_if_both_are_letters(self):
    assert same_category("a", "B") is True

  def test_returns_true_if_both_are_numbers(self):
    assert same_category("1", "3") is True

  def test_returns_false_if_not_from_same_category(self):
    assert same_category("1", "B") is False

  def test_0_is_admitted_in_numbers(self):
    assert same_category("0", "9") is True
    assert same_category("9", "0") is True

class TestDetectSequences:

  def test_invalid_if_password_isnt_str(self):
    with pytest.raises(TypeError):
      detect_sequences(1234)

  def test_invalid_if_min_len_is_not_a_number(self):
    with pytest.raises(TypeError):
      detect_sequences("Avc", "bac")

  def test_is_invalid_if_min_len_is_below_3(self):
    with pytest.raises(ValueError):
      detect_sequences("abc", 2)

  def test_returns_empty_list_if_password_is_empty(self):
    assert detect_sequences("") == []

  def test_no_sequences(self):
    result = detect_sequences("aaa")
    assert result == []

  def test_works_under_normal_circumstances(self):
    password = "abcX9876"
    assert detect_sequences(password) == [
      {'type': 'ascending_sequence', 'value': 'abc', 'start': 0, 'end': 3, 'length': 3},
      {'type': 'descending_sequence', 'value': '9876', 'start': 4, 'end': 8, 'length': 4}
    ]

  def test_returns_nothing_if_there_is_no_sequence(self):
    password = "a1b2c3"
    assert detect_sequences(password) == []

  def test_respects_min_len_amount(self):
    password = "abcX1234"
    assert detect_sequences(password, 4) == [
      {'type': 'ascending_sequence', 'value': '1234', 'start': 4, 'end': 8, 'length': 4}
    ]

  def test_works_with_number_sequence(self):
    password = "123Aavb"
    assert detect_sequences(password) == [
      {'type': 'ascending_sequence', 'value': '123', 'start': 0, 'end': 3, 'length': 3}
    ]

  def test_works_when_sequence_at_end(self):
    password = "xyzwxyz"
    assert detect_sequences(password) == [
      {'type': 'ascending_sequence', 'value': 'xyz', 'start': 0, 'end': 3, 'length': 3},
      {'type': 'ascending_sequence', 'value': 'wxyz', 'start': 3, 'end': 7, 'length': 4}
    ]

  def test_returns_nothing_when_only_one_char(self):
    password = "a"
    assert detect_sequences(password) == []

  def test_works_when_the_password_is_the_sequence(self):
    password = "abc"
    assert detect_sequences(password) == [
      {'type': 'ascending_sequence', 'value': 'abc', 'start': 0, 'end': 3, 'length': 3}
    ]

  def test_raises_error_when_min_len_is_bool(self):
    with pytest.raises(TypeError):
      detect_sequences("adawa", True)

  def test_works_well_with_descending_sequences(self):
    password = "CbA4324"
    assert detect_sequences(password) == [
      {'type': 'descending_sequence', 'value': 'CbA', 'start': 0, 'end': 3, 'length': 3},
      {'type': 'descending_sequence', 'value': '432', 'start': 3, 'end': 6, 'length': 3}
    ]

  def test_works_when_the_same_char_is_in_two_sequences(self):
    password = "abcdCBA"
    assert detect_sequences(password) == [
      {'type': 'ascending_sequence', 'value': 'abcd', 'start': 0, 'end': 4, 'length': 4},
      {'type': 'descending_sequence', 'value': 'dCBA', 'start': 3, 'end': 7, 'length': 4}
    ]

class TestRepeatedSubstring:
  def test_detects_repeated_substring(self):
    password = "aacaac"
    assert detect_repeated_substrings(password) == [
      {'type': 'repeated_substring', 'value': 'aac', 'start': 0, 'end': 6, 'length': 6, 'repetitions': 2}
    ]
  def test_detects_smallest_repeating_pattern(self):
    password = "abababab"
    assert detect_repeated_substrings(password) == [
      {'type': 'repeated_substring', 'value': 'ab', 'start': 0, 'end': 8, 'length': 8, 'repetitions': 4}
    ]
  def test_detects_overlapping_repeated_patterns(self):
    password = "abababcabcabc"
    assert detect_repeated_substrings(password) == [
      {'type': 'repeated_substring', 'value': 'ab', 'start': 0, 'end': 6, 'length': 6, 'repetitions': 3},
      {'type': 'repeated_substring', 'value': 'abc', 'start': 4, 'end': 13, 'length': 9, 'repetitions': 3}
    ]
  def test_detects_longest_repetition_with_smallest_pattern(self):
    password = "aabaab"
    assert detect_repeated_substrings(password) == [
      {"type": "repeated_substring", "value": "aab", "start": 0, "end": 6, "length": 6, "repetitions": 2}
    ]
  def test_invalid_if_password_is_empty(self):
    with pytest.raises(ValueError):
      assert detect_repeated_substrings("")

  def test_invalid_if_password_is_not_string(self):
    with pytest.raises(TypeError):
      assert detect_repeated_substrings(112)

  def test_invalid_if_min_is_invalid(self):
    with pytest.raises(ValueError):
      assert detect_repeated_substrings("ada", 0)


class TesteIsRedundantPattern:
  def test_redundant_same_pattern(self):
    sequences = [{"value": "ab", "start": 0, "end": 8}]
    candidate = {"value": "ab", "start": 2, "end": 8}
    assert is_redundant_pattern(candidate, sequences) is True

  def test_redundant_shifted_pattern(self):
    sequences = [{"value": "ab", "start": 0, "end": 8}]
    candidate = {"value": "ba", "start": 1, "end": 7}
    assert is_redundant_pattern(candidate, sequences) is True

  def test_overlapping_patterns_are_not_redundant(self):
    sequences = [{"value": "ab", "start": 0, "end": 6}]
    candidate = {"value": "abc", "start": 4, "end": 13}
    assert is_redundant_pattern(candidate, sequences) is False

  def test_separate_patterns_are_not_redundant(self):
    sequences = [{"value": "ab", "start": 0, "end": 4}]
    candidate = {"value": "ab", "start": 5, "end": 9}
    assert is_redundant_pattern(candidate, sequences) is False

  def test_empty_sequences(self):
    candidate = {"value": "ab", "start": 0, "end": 4}
    assert is_redundant_pattern(candidate, []) is False