# input range of array
n = int(input())

# input array and split the input
arr = list(map(int, input().rstrip().split()))

# reverse array
b=arr[::-1]

# print array
for c in range(len(b)):
	print(b[c], end='')
	print(" ", end='')
