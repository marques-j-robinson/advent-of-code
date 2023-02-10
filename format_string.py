def get_char_count(s):
	chars = {}
	for i in s:
		if i in chars.keys():
			chars[i] += 1
		else:
			chars[i] = 1
	return chars


def remove_diff_chars(s1, s2):
	res = ''
	for idx, char in enumerate(s1):
		if char == s2[idx]:
			res += char
	return res


def leading_zero(n):
    return str(n).zfill(2)
