# https://leetcode.com/problems/roman-to-integer/description/
# Method 1:
def roman_to_int(s):
  roman_to_int_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  result = 0
  mapped = [roman_to_int_dict[x] for x in s]
  for i in range(len(mapped)):
    if i < len(mapped) - 1 and mapped[i + 1] > mapped[i]:
      result -= mapped[i]
    else:
      result += mapped[i]
  return result

# Method 2:
def roman_to_int(s):
  roman_to_int_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  result = 0
  for i, letter in enumerate(s):
    if i < len(s) - 1 and roman_to_int_dict[s[i + 1]] > roman_to_int_dict[s[i]]:
      result -= roman_to_int_dict[letter]
    else:
      result += roman_to_int_dict[letter]
  return result

# Method 3: even though more lengthy, gives shorter run-time.
def roman_to_int(s):
  roman_to_int_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  result = 0
  for i, letter in enumerate(s):
    if letter == "I" and i != len(s) - 1 and s[i + 1] in ["V", "X"]:
        result -= 1
    elif letter == "X" and i != len(s) - 1 and s[i + 1] in ["L", "C"]:
        result -= 10
    elif letter == "C" and i != len(s) - 1 and s[i + 1] in ["D", "M"]:
        result -= 100
    else:
      result += roman_to_int_dict[letter]
  return result
print(roman_to_int("MCMXCIV"))

