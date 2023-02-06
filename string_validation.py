def differ_by_exactly_one_char(s1, s2):
	diffs = 0
	for idx, i in enumerate(s2):
		j = s1[idx]
		if i != j:
			diffs += 1
	return diffs == 1
