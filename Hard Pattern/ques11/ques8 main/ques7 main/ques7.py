n = int(input())
if n < 1 or n % 2 == 0:
    exit(0)

for i in range(n // 2 + 1):
    print(" " * (n // 2) + " " * i + "@" * (n - 2 * i))

for i in range(n):
    for j in range(n + 1):
        if i == 0 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    
"""
 @@@@@
   @@@
    @
******
*   * 
*   * 
*   * 
*   * 
  """
