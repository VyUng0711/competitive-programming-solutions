# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2003
# 1st solution:
text = ""
while True:
  try:
    this_line = input()
    if this_line != "":
      if this_line[-1] == '-':
        text += this_line[:-1]
      else:
        text += this_line + " "
  except EOFError:
    break
    
  out_text = ""
  for letter in text:
    if letter.isalpha() or letter == '-' or letter == ' ':
      out_text += letter
    else:
      out_text += ' '
  ans = set([w.lower() for w in out_text.split()])
print(*sorted(ans), sep = "\n")

# 2nd solution:
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
