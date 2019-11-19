# Receiving input how many input are inserted / sorry for my bad english
N = int(input())

# For every i in range 0 to N, N = input
for i in range(0, N):

	# input string
	S = input()

	# For every j in range 0 to length of the S (String)
	for j in range(0, len(S)):

		# If j%2 = even
		if j%2 == 0:

			# Print even array of S
			# by using end='', it won't create new line
			print(S[j], end='')
	
	# Print space without new line
	print(" ", end='')

	# For every j in range 0 to length of the S (string)	
	for j in range(0, len(S)):

		# if j%2 is not even (odd)
		if j%2 != 0:

			# Print odd array of S
			print(S[j], end='')
	print("")	
