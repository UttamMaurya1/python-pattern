''' Star Pattern'''

'''
*
**
***
****
*****'''
# n=int(input("Enter a no.: "))
# for i in range (1, n+1):
#     print("*"* i, end="")
#     print("")

# row=int(input("Enter a no.: "))
# for i in range (1, row+1):
#     print("*"* i)

'''
*****
****
***
**
*
'''
# rows = int(input("Enter the number of rows: "))

# for i in range(rows, 0, -1):
#     print('*' * i)

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
# n=int(input("Enter a no.: "))
# for i in range (1, n+1):
#     for j in range (n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print("")    

# size = 5
# # Upper part
# for i in range(size):
#     for j in range(size - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()
# # Lower part
# for i in range(size - 2, -1, -1):
#     for j in range(size - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()


'''Imp'''

# # Initialize a list to store the inputs
# inputs = []

# # Loop to take four inputs from the user
# for i in range(4):
#     user_input = input(f"Enter string {i + 1}: ")
#     inputs.append(user_input)

# # Check each input and print the required information
# for string in inputs:
#     print(f"You entered: {string}")
#     if 'ab' in string and len(string) == 4:
#         print(f"The string '{string}' contains 'ab' and its length is 4.")
#     else:
#         print(f"The string '{string}' either does not contain 'ab' or its length is not 4.")


# * 
# * *
# * * *
# * * * *
# * * * * *
# n=int(input("Enter a no."))
# for i in range (n):
#     for j in range (i+1):
#         print('*', end=' ')
#     print ()

# * * * * * 
# * * * *
# * * *
# * *
# *
# n=int(input("Enter a no:"))
# for i in range (n):
#     for j in range (i,n):
#         print ("*", end=" ")
#     print ()

#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
# n=int(input("Enter a no:"))
# for i in range (n):
#     for j in range (i,n):
#         print (" " , end=" ")
#     for j in range (i+1):
#         print ("*", end=" ")
#     print ()

#   * * * * * 
#     * * * *
#       * * *
#         * *
#           *
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range (i+1):
#         print(" ", end=" ")
#     for j in range (i,n):
#         print("*", end=" ")
#     print ()

#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *   
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for k in range (i-0): 
#         print("*", end=" ")
#     print() 

# * * * * * * * * *
#  * * * * * * *
#   * * * * *
#     * * *
#       *
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     for k in range (i+1,n): 
#         print("*", end=" ")
#     print() 


#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
# n=int(input("Enter a no: "))
# for i in range (n-1):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     for k in range (i-0): 
#         print("*", end=" ")
#     print() 
# for i in range (n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     for k in range (i+1,n): 
#         print("*", end=" ")
#     print() 

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *     
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range (i,n):
#         print(" ", end="")
#     for j in range (i+1):
#         print("*", end=" ")
#     print ()

# * 
# * *
# * * *
# * * * *
# * * * * *
# n=int(input("enter a no: "))
# for i in range (n):
#     for j in range (i+1):
#         print("*",end=" ")
#     print()

#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
# n=int(input("enter a no: "))
# for i in range (n):
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i+1):
#         print("*",end=" ")
#     print()

# * * * * * 
# * * * *
# * * *
# * *
# *
# n=int(input("enter a no: "))
# for i in range (n):
#     for j in range (i,n):
#         print("*",end=" ")
#     print()

#   * * * * * 
#     * * * *
#       * * *
#         * *
#           *
# n=int(input("enter a no: "))
# for i in range (n):
#     for j in range (i+1):
#         print(" ",end=" ")
#     for j in range (i,n):
#         print("*",end=" ")
#     print()

#      *       * 
#     * *     * *
#    * * *   * * *
#   * * * * * * * *
#  * * * * * * * * *
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range (i+2,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         if(j<n-1):
#             print("*",end=" ")
#     print()

#  * * * * * 
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("Enter a no:"))
# for i in range (n):
#     for i in range (i+1):
#         print(" ",end="")
#     for i in range (i,n):
#         print("*", end=" ")
#     print()

# *           * 
# * *       * *
# * * *   * * *
# * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
# n = int(input("Enter a number: "))
n=6

for i in range(n - 1):
    for j in range(i + 1):
        print("*", end=" ")
    for j in range(2 * (n - i - 2) - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        if(j<n-2):
            print("*", end=" ")
    print()
for i in range(1, n):
    for j in range(n - i):
        print("*", end=" ")
    for j in range(2 * i - 1):
        print(" ", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()

''' Number Pattern'''

# 1 
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
# n=int(input("Enter a no: "))
# p=1
# for i in range (n):
#     for j in range (i+1):
#         print(p,end=" ")
#     print()

# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# n=int(input("Enter a no: "))
# p=1
# for i in range (n):
#     for j in range (i+1):
#         print(p,end=" ")
#     p+=1
#     print()

# 5 
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
# n=int(input("Enter a no: "))
# p=5
# for i in range (n):
#     for j in range (i+1):
#         print(p,end=" ")
#     p-=1
#     print()

# 0
# 2 2
# 4 4 4
# 6 6 6 6
# 8 8 8 8 8
# n=int(input("Enter a no: "))
# p=0
# for i in range (n):
#     for j in range (i+1):
#         print(p,end=" ")
#     p+=2
#     print()

# 1 
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range (i+1):
#         if(i%2==0):
#             print("1",end=" ")
#         else:
#             print("2",end=" ")
#     print()

#           1 
#         2 2 2
#       3 3 3 3 3
#     4 4 4 4 4 4 4
#   5 5 5 5 5 5 5 5 5
#     6 6 6 6 6 6 6
#       7 7 7 7 7
#         8 8 8
#           9
# n=int(input("Enter a no: "))
# p=1
# for i in range (n-1):
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i+1):
#         print(p,end=" ")
#     for j in range (i+0):
#         print(p,end=" ")
#     p+=1
#     print()
# for i in range (n):
#     for j in range (i+1):
#         print(" ",end=" ")
#     for j in range (i,n):
#         print(p,end=" ")
#     for j in range (i+1,n):
#         print(p,end=" ")
#     p+=1
#     print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=1 
#     for j in range (i+1):
#         print(p,end=" ")
#         p+=1
#     print()

#   1 2 3 4 5 
#     1 2 3 4
#       1 2 3
#         1 2
#           1
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=1 
#     for j in range (i+1):
#         print(" ",end=" ")
#     for j in range (i,n):
#         print(p,end=" ")
#         p+=1
#     print()

#           1 
#         1 2 3
#       1 2 3 4 5
#     1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8 9
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=1 
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i+1):
#         print(p,end=" ")
#         p+=1
#     for j in range (i+0):
#         print(p,end=" ")
#         p+=1
#     print()

#   5 4 3 2 1 
#     4 3 2 1
#       3 2 1
#         2 1
#           1
# n=int(input("Enter a no:"))
# k=5
# for i in range (n):
#     p=k
#     for j in range (i+1):
#         print(" ",end=" ")
#     for j in range (i,n):
#         print(p,end=" ")
#         p-=1
#     k-=1    
#     print()

#           1 
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=1
#     for j in range (i,n):
#         print(" ",end=" ")
#     for j in range (i):
#         print(p,end=" ")
#         p+=1
#     for j in range (i+1):
#         print(p,end=" ")
#         p-=1
#     print()

# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# n=int(input("Enter a no: "))
# p=1
# for i in range (n):
#     for j in range (i+1):
#         print(p,end=" ")
#         p+=1
#     print()

''' Alphabet Pattern'''

# A 
# A A
# A A A
# A A A A
# A A A A A
# n=int(input("Enter a no: "))
# p=65
# for i in range (n):
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     print()

# A 
# B B
# C C C
# D D D D
# E E E E E
# n=int(input("Enter a no: "))
# p=65
# for i in range (n):
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()

# E 
# D D
# C C C
# B B B B
# A A A A A
# n=int(input("Enter a no: "))
# p=69
# for i in range (n):
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p-=1
#     print()

# A 
# C C
# E E E
# G G G G
# I I I I I
# n=int(input("Enter a no: "))
# p=65
# for i in range (n):
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=2
#     print()

# A 
# C C
# E E E
# G G G G
# I I I I I
# n=int(input("Enter a no: "))
# p=65
# for i in range (n):
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=2
#     print()

# A 
# B B
# A A A
# B B B B
# A A A A A
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range (i+1):
#         if (i%2==0):
#             print(chr(65),end=" ")
#         else:
#             print(chr(66),end=" ")
#     print()

# Z Z Z Z Z 
#   0 0 0 0
#     Z Z Z
#       0 0
#         Z
# n=int(input("Enter a no: "))
# for i in range (n):
#     for j in range (i):
#         print(" ",end=" ")
#     for j in range (i,n):
#         if (i%2==0):
#             print('Z',end=" ")
#         else:
#             print(0,end=" ")
#     print()

#           A 
#         B B B
#       C C C C C
#     D D D D D D D
#   E E E E E E E E E
#     F F F F F F F
#       G G G G G
#         H H H
#           I
# n=int(input("Enter a no: "))
# p=65
# for i in range (n-1):
#     for j in range (i,n):
#         print(" ", end=" ")
#     for j in range (i):
#         print(chr(p),end=" ")
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
# for i in range (n):
#     for j in range (i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print(chr(p),end=" ")
#     for j in range(i+1,n):
#         print(chr(p),end=" ")
#     p+=1
#     print()
        
#           A 
#         B B B
#       C C C C C
#     D D D D D D D
#   A A A A A A A A A
#     B B B B B B B
#       C C C C C
#         D D D
#           E
# n=int(input("Enter a no: "))
# p=65
# for i in range (n-1):
#     for j in range (i,n):
#         print(" ", end=" ")
#     for j in range (i):
#         print(chr(p),end=" ")
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
# p=65
# for i in range (n):
#     for j in range (i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print(chr(p),end=" ")
#     for j in range(i+1,n):
#         print(chr(p),end=" ")
#     p+=1
#     print()

#           A 
#         B B B
#       C C C C C
#     D D D D D D D
#   E E E E E E E E E
#     D D D D D D D
#       C C C C C
#         B B B
#           A
# n=int(input("Enter a no: "))
# p=65
# for i in range (n-1):
#     for j in range (i,n):
#         print(" ", end=" ")
#     for j in range (i):
#         print(chr(p),end=" ")
#     for j in range (i+1):
#         print(chr(p),end=" ")
#     p+=1
#     print()
# for i in range (n):
#     for j in range (i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print(chr(p),end=" ")
#     for j in range(i+1,n):
#         print(chr(p),end=" ")
#     p-=1
#     print()

# A 
# A B
# A B C
# A B C D
# A B C D E
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=65
#     for j in range (i+1):
#         print(chr(p),end=" ")
#         p+=1
#     print()

# A B C D E 
#   A B C D
#     A B C
#       A B
#         A
# n=int(input("Enter a no: "))
# for i in range (n):
#     p=65
#     for j in range (i):
#         print(" ",end=" ")
#     for j in range (i,n):
#         print(chr(p),end=" ")
#         p+=1
#     print()

# C 
# O O
# D D D
# E E E E
# R R R R R
# s="CODER"
# n=len(s)
# p=0
# for i in range (n):
#     for j in range (i+1):
#         print(s[p], end=" ")
#     p+=1
#     print()

# R 
# E E
# D D D
# O O O O
# C C C C C
s="CODER"
n=len(s)
p=n-1
for i in range (n):
    for j in range (i+1):
        print(s[p], end=" ")
    p-=1
    print() 
