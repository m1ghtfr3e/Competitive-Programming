#!/usr/bin/env python

def filter_list(l):

	result = []
	for filter in l:
		if type(filter) is int:
			result.append(filter)
	return result


print(filter_list([1, 2, 'a', 'b']))


