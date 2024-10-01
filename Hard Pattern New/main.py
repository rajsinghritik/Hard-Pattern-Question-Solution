"""""
Ques-1
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
               CODING
for i in range(1,6):
    for j in range(1,6):
       print("*", end=" ")
       
    print()
    """
    
"""""
Ques-2
*
**
***
****
*****
           CODING     
r=5
for i in range(1,r+1):
    for j in range(1,i+1):
        print("*" , end="")
    print()  
      
    """""
"""""
Ques=3
* * * * *
* * * *
* * *
* *
*
              CODING 
n=5    
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    
  """""
"""""
Ques-4
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
         CODING 
n=6
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")  
    print()    
     
     """""
""""" 
Ques-5
6 5 4 3 2 1 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
   CODING  
n = 6
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()       
    """""
""""" 
Ques-6
      *
     ***
    *****
   *******
  *********
            CODING 
num = int(input("Enter the number of num: ")) 
for i in range (num):
    for j in range(num-i):
        print("",end=" ")
    for j in range(2*i+1):
            print("*", end="")
    print()
    """""         
""""

*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
n=int(input('Enter the number of n:: '))

for i in range(n,0,-1):                    
    for j in range(n-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
    print()    
            """
            
"""

*                 *
 *               * 
  *             *  
   *           *   
    *         *    
     *       *     
      *     *      
       *   *       
        * *        
         *         
        * *        
       *   *       
      *     *      
     *       *     
    *         *    
   *           *   
  *             *  
 *               * 
*                 *
n = int(input('Enter the value of n: '))

for i in range(1,2*n):
    for j in range(1,2*n):
        if i==j or i+j==2*n:
            print('*', end='')
        else:
            print(' ', end='')
    print()
     """            
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 

row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(i+1):
        print('*',end=' ')
    print()
       """ 
"""

* 
* * 
*   * 
*     * 
*       * 
*         * 
*           * 
* * * * * * * *
row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(i+1):
        if j==0 or j==i or i==row-1:
            print('*',end=" ")
        else:
            print(" ", end=" ")
    print()
   """       
   
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


number = int(input('Enter number: '))


if(number< 0):
    print('Factorial does not exist!')
else:
     print('Factorial of %d is %d' %(number,factorial(number) ))
     """ 