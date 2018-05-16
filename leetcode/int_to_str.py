def int_to_str(x):
	is_negative = False
	if x < 0:
		x, is_negative = -x, True
	s = []
	while True:
		temp = chr(ord('0') + x % 10)
		print (temp)
		s.append(temp)
		x //= 10
		if x == 0:
			break
	return ('-' if is_negative else '') + ''.join(reversed(s))
#print (int_to_str(345))
print (ord('0'))
#print (chr(ord('0') + 5))