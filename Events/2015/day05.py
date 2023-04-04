from main import CacheLayer


vowels = 'aeiou'
forbidden = ['ab', 'cd', 'pq', 'xy']


def check_dup(s):
	res = False
	for idx, l in enumerate(s):	
		if idx > 0 and l == s[idx-1]:
			res = True
	return res


def calc_vowel_count(s):
	res = 0
	for l in s:
		if l in vowels:
			res += 1
	return res


def check_forbidden(s):
	res = False
	for f in forbidden:
		if f in s:
			res = True
	return res


def dup_pairs(s):
        res = False
        for idx, l in enumerate(s):
            if idx > 0:
                pair = f"{s[idx - 1]}{l}"
                if pair in s[idx + 1:]:
                    res = True
        return res


def repeat_every_other_letter(s):
    res = False
    for idx, l in enumerate(s):
        if idx > 1:
            prev = s[idx - 2]
            if prev == l:
                res = True
    return res


class S(CacheLayer):

	def solve(self):
		self.split_by_new_line()
		for s in self.puzzle_input:
			if check_forbidden(s) is False:
				if calc_vowel_count(s) >= 3:
					if check_dup(s) is True:
						self.p1 += 1
			if dup_pairs(s) is True:
				if repeat_every_other_letter(s) is True:
					self.p2 += 1
