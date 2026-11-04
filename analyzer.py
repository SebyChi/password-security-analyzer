def analyze_password(password):
  return {
    "length": len(password),
    "has_uppercase": any(c.isupper() for c in password),
    "has_lowercase": any(c.islower() for c in password),
    "has_digit": any(c.isdigit() for c in password),
    "has_special": any(not c.isalnum() for c in password)
  }



