
def read_matx():
	matx = []
	for i in range(3):
		row = list(map(int,input().split()))
		matx.append(row)
	return matx

def print_matx(m):
	for row in range(1):
		print (*m[row])

m = read_matx()
print_matx(m)