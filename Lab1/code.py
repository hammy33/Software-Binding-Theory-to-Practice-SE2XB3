def are_valid_groups(sNums, groups):
	for i in groups:
		if len(i) not in [2, 3]: return False
	return True if len(sNums) == len(set(sNums)) else False
