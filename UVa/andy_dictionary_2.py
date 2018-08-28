# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2003
import string
alphabet = set(string.ascii_lowercase)
alphabet.add('-')

text_input = []
not_alphabet = set()
while True:
  try:
    this_line = input()
    for letter in this_line:
      if letter.lower() not in alphabet:
        not_alphabet.add(letter.lower())

    for word in this_line.split():
      text_input.append(word.lower())
  except EOFError:
    break
new_word = True
merged = ''
text_output = set()

for t in text_input:
  if t[-1] == '-':
    new_word = False
    merged += t[:-1]
  else:
    if new_word == True:
      for na in not_alphabet:
        t = t.replace(na, " ")
      ss = t.split()
      for s in ss:
        text_output.add(s)
    else:
      merged += t
      for na in not_alphabet:
        merged = merged.replace(na, " ")
      mm = merged.split()
      for m in mm:
        text_output.add(m)
      new_word = True
      merged = ''
    
text_output = sorted(text_output)
print(*text_output,sep='\n')