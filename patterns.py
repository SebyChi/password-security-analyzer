def repeated_chars(password, min_repetitions = 2):
  if type(password) != str:
    raise TypeError("Password is invalid")
  if type(min_repetitions) != int:
      raise TypeError("Please input a number")
  if min_repetitions < 2:
    raise ValueError("No numbers below 2")
  repetitions = []
  if not password:
    return repetitions
  start = 0
  end = 1
  while start < len(password):
    while end <= len(password)-1 and password[start] == password[end]:
      end+=1
    if end-start >= min_repetitions:
      repetitions.append({"type" : "repeated_char", "value" : password[start:end], "start": start, "end" : end, "length" : end-start})
    start = end
    end+=1
  return repetitions

"""
print(repeated_chars("aaaa"))
print(repeated_chars("aaab"))
print(repeated_chars("a"))
print(repeated_chars("abc"))
print(repeated_chars("aabb", 3))
print(repeated_chars("aaaAAbCCc"))
print(repeated_chars("aaabb"))
print(repeated_chars("aab"))
print(repeated_chars("aabb"))
"""

