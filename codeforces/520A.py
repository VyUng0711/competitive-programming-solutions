import string

def pangram(input_string):
  return 'YES' if len(set(input_string.lower())) == 26 else 'NO'


def pangram_1(input_string):
  return 'YES' if all(x in input_string.lower() for x in string.ascii_lowercase) else 'NO'

def pangram_2(input_string):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  input_string = input_string.lower().strip()
  letter_dict = [0] * 26
  for letter in input_string:
    letter = ord(letter) - ord('a')
    letter_dict[letter] = 1
  if sum(letter_dict) < 26:
    return "NO"
  else:
    return "YES"

def pangram_3(input_string):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  input_string = input_string.lower().strip()
  letter_dict = {}
  for letter in input_string:
    if letter in letter_dict:
      letter_dict[letter] += 1
    else:
      letter_dict[letter] = 1
  for i in alphabet:
    if i not in letter_dict:
      return "NO"
  return "YES"
n = int(input())
s = input()
print(pangram(s))
  