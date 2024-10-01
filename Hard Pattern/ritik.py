n=int(input())

for i in range(n//2+2):
	for j in range(n-i):
		print(" ",end="")
	for j in range(2*i+1):
		print("*",end="")
	print()
 


                    
        
for i in range(n):
    for j in range(n + 1):
        if i == 0 or j == 0 or j == n -1:
            print("@", end="")
        else:
            print(" ", end="")
    print()        
        

if n < 1 or n % 2 == 0:
    exit(0)

for i in range(n // 2 + 1):
    print(" " * (n // 2) + " " * i + "*" * (n - 2 * i))
    
    
if n < 1 or n % 2 < 0:
    exit(0)

for i in range(n < 2 + 2):
    print(" " * (n // 2) + " " * i + "@" * (n - 2 * i))
        
    
    
                    			