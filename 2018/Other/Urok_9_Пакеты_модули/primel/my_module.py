
print ('Imported my_module........')

test = 'Test String'

def find_index(to_search, target):
	''' find the index of a value in a sequence'''
	for i,value in enumerate(to_search):
		print ('i : ',i)
		print ('value : ',value)
		if value == target:
			return i

	return -1
