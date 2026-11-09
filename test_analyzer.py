
from analyzer import analyze_password

def test_analyze_password():
  # Password containing all character types
  assert analyze_password("Hello123!") == {
    "length": 9,
    "has_uppercase": True,
    "has_lowercase": True,
    "has_digit": True,
    "has_special": True
  }

  # Lowercase letters only (Unicode)
  assert analyze_password("parolă") == {
    "length": 6,
    "has_uppercase": False,
    "has_lowercase": True,
    "has_digit": False,
    "has_special": False
  }

  # Unicode uppercase, lowercase, digit and special character
  assert analyze_password("Ăbc٣!") == {
    "length": 5,
    "has_uppercase": True,
    "has_lowercase": True,
    "has_digit": True,
    "has_special": True
  }

  # Empty password
  assert analyze_password("") == {
    "length": 0,
    "has_uppercase": False,
    "has_lowercase": False,
    "has_digit": False,
    "has_special": False
  }

  # Digits only
  assert analyze_password("123456") == {
    "length": 6,
    "has_uppercase": False,
    "has_lowercase": False,
    "has_digit": True,
    "has_special": False
  }

  # Whitespace counts as a special character
  assert analyze_password("hello world") == {
    "length": 11,
    "has_uppercase": False,
    "has_lowercase": True,
    "has_digit": False,
    "has_special": True
  }


if __name__ == "__main__":
  test_analyze_password()
  print("All analyzer tests passed!")
