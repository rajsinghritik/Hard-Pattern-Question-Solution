# Python3 implementation
n=int(input())

for i in range(n//2+2):
	for j in range(n-i):
		print(" ",end="")
	for j in range(2*i+1):
		print("@",end="")
	print()

for i in range(n):
    for j in range(n//2+1):
	     if (j>=n//2-i and j>=i-n//2):
			  print("*",end="")
	    else:
			print(" ",end="")
	for j in range(n):
		if i==n//2:
			print("@",end="")
		else:
			print(" ",end="")
	for j in range(n//2+1):
		if (j>=n//2-i and j>=i-n//2):
			print("*",end="")
	print()

	"""
     @
    @@@
   @@@@@
  @@@@@@@
  *     *
 **     **
***@@@@@***
 **     **
  *     *
 
 
	"""