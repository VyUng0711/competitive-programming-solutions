
def regular_bracket_sequence(brackets):
  wrong_open = []
  wrong_close = []
  for i in range(len(brackets)):
    if brackets[i] == "(":
      wrong_open.append(i)
    else:
      if len(wrong_open) > 0:
        wrong_open.pop()
      else:
        wrong_close.append(i)
  return(len(brackets) - len(wrong_open) - len(wrong_close))
   
b = input()
print(regular_bracket_sequence(b))