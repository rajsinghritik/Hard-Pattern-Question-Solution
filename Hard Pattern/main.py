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
num = int(input("Enter the number of rows: ")) 
for i in range (0,num):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(0,2*i+1):
            print("*", end="")
    print()
    """""         