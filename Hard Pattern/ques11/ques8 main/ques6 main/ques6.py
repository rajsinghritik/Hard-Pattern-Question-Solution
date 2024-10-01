n = 6
x = 0
for i in range(2 * n):
    flag = False
    if i < n + 1:
        print("@", end="")
    else:
        print(" ", end="")
        
    
    for j in range(n * (n - 1) + 1):
        if n // 2 <= i < 2 * n - n // 2:
            if j < (n - 1) * x or j > (n - 1) * x + n - 1:
                print(" ", end="")
            else:
                print("*", end="")
            flag = True
           
        else:
            print(" ", end="")
    
    if flag:
        x += 1
    if i >= n - 1:
        print("@", end="")
    else:
        print(" ", end="")
    
    print()

""""
@
@
@
@******
@     ******
@          ******               @
@               ******          @
                     ******     @
                          ******@
                                @
                                @
                                @
                                """