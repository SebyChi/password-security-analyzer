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

def same_category(char1, char2):
  same = False
  if 'a' <= char1.lower() <= 'z' and 'a' <= char2.lower() <= 'z':
    same = True
  if '0' <= char1 <= '9' and '0' <= char2 <= '9':
    same = True
  return same

def get_sequence_direction(char1, char2):
  if type(char1) != str:
    raise TypeError("Not a character")
  if type(char2) != str:
    raise TypeError("Not a character")
  if len(char1) != 1:
    raise ValueError("Invalid character1")
  if len(char2) != 1:
    raise ValueError("Invalid character2")
  order = 0
  if same_category(char1, char2) and ord(char1.lower()) - ord(char2.lower()) == -1:
    order = 1
  elif same_category(char1, char2) and ord(char1.lower()) - ord(char2.lower()) == 1:
    order = -1
  return order

def detect_sequences(password, min_len = 3):
  if type(password) != str:
    raise TypeError("Password is invalid")
  if type(min_len) != int:
    raise TypeError("Please input a number")
  if min_len < 3:
    raise ValueError("No numbers below 3")
  sequences = []
  if not password:
    return sequences  
  start = 0
  end = 1
  while start < len(password) and end < len(password):
    c = get_sequence_direction(password[start], password[end])
    while c!=0 and end<len(password)-1 and c == get_sequence_direction(password[end], password[end+1]) :
      end+=1
    if end-start+1 >= min_len:
      if c==1:
        sequences.append({"type" : "ascending_sequence", "value" : password[start:end+1], "start" : start, "end" : end+1, "length" : end-start+1})
      else:
        sequences.append({"type" : "descending_sequence", "value" : password[start:end+1], "start" : start, "end" : end+1, "length" : end-start+1})
    start = end
    end = end+1
  return sequences

def detect_repeated_substrings(password, min_length=2):
  if type(password) != str:
      raise TypeError("Password is invalid")
  if type(min_length) != int:
      raise TypeError("Minimum length must be an integer")
  if min_length < 2:
      raise ValueError("Minimum length must be at least 2")

  sequences = []
  start = 0

  while start < len(password):
    max_size = (len(password) - start) // 2
    found = False
    for size in range(min_length, max_size + 1):
      pattern = password[start:start + size]
      repetitions = 1
      while start + (repetitions + 1) * size <= len(password):
        next_block = password[
          start + repetitions * size:
          start + (repetitions + 1) * size
        ]
        if pattern != next_block:
          break
        repetitions += 1
        candidate = {}
      if repetitions >= 2:
        end = start + repetitions * size
        candidate = {
          "type": "repeated_substring",
          "value": pattern,
          "start": start,
          "end": end,
          "length": repetitions * size,
          "repetitions": repetitions
        }

        if not is_redundant_pattern(candidate, sequences):
          sequences.append(candidate)

        start += 1
        found = True
        break

    if not found:
      start += 1

  return sequences


def is_redundant_pattern(candidate, sequences):
  for sequence in sequences:
    if (
      sequence["start"] <= candidate["start"]
      and sequence["end"] >= candidate["end"]
    ):
      return True

  return False
