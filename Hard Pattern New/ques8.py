n = 9
for i in range(n):
    for j in range(n):
        if (i < n // 2 and j <= i) or (i > n // 2 and j < n - i) or (i == n // 2):
            print("*", end="")
        else:
            print(" ", end="")
    if i == n // 2 - 1 or i == n // 2 + 1:
        print(" *", end="")
    if i == n // 2:
        print("***", end="")
    print()
    
    """
*        
**       
***      
****      *
************
****      *
***      
**       
*  
"""