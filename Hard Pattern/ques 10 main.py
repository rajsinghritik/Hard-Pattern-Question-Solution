n=int(input())
for i in range(n//2+1):
    for j in range(n):
        print(" ",end="")
    for j in range(n//2-i):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
    
    for i in range(n-2):
        for j in range(n):
            print(" ",end="")
        for j in range(n):
          if j<n:
            if j==0 or j==n-1:
              print("@",end="")
            else:
              print(" ",end="")
                    
        print()                            
    
for i in range(n//2+1):
  for j in range(n//2):
    if j<1:
        print(" ",end="")
    for j in range(n-(2*i)):
        print("*",end="")
    for j in range(n//2):
        if j<i:
           print(" ",end="")
            
    for j in range(n):
      if i==0 and (j==0 or j==n-1):
            print("@",end="")
      else:
        print(" ",end="")
            
    for j in range(n//2):
      if j<1:
        print(" ",end="")
    for j in  range(n-(2*i)):
      print("*",end="")
    print()                        
                                    
                                    