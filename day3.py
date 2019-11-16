# receiving input integer
n = int(input())

# if n is odd, print Weird
if (n % 2) != 0:
	print("Weird")

# if n is even and in the inclusive range of 2 to 5, print Not Weird
elif (n%2 == 0 and n>=2 and n<=5):
	print("Not Weird")

#if n is even and in the inclusive range of 6 to 20 print Weird
elif (n%2 == 0 and n>=6 and n<=20):
	print("Weird")

#if n is even and greater than 20, print Not Weird
elif (n%2 == 0 and n>20 and n<=100):
	print("Not Weird")

	
