# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1756
import string
alphabet = set(string.ascii_lowercase)
text_input = set()
while True:
  try:
    this_line = Scanner.next()
    for letter in this_line:
      if letter.lower() not in alphabet:
        # print(letter)
        this_line = this_line.replace(letter.lower(), " ")
    for word in this_line.split():
      text_input.add(word.lower())
  except EOFError:
    break
text_output = sorted(text_input)
print(*text_output,sep='\n')
