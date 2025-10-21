def printPattern(n):
    for i in range(0, n):
        for j in range(0, n):
            if (i == 0 or j == 0 or i == n-1 or j == n-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print() 

def printPlus(n):
    for i in range(n):
        for j in range(n):
            if(i== n//2 or j==n//2):
                print("*",end="")
            else:
                print(" ",end="")
        print()

# printPlus(7)
# printPattern(5)

def diamondPattern():
   n=int(input("Please Enter the number you want : "))
 
   for i in range(1,n+1):
     #for upper body of pattern
     for j in range(1,n-i+1):
         print(" ",end="")
     for k in range(1,2*i):
         print("*",end="")
     print()
   for i in range(n,1,-1):
       for j in range(1,n-i+1):
           print(" ",end="")
       for k in range(1,2*i):
         print("*",end="")
       print()
 
 
diamondPattern()