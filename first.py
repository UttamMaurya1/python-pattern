# Chapter 2 practice

# Q1 Write a python program to add two no.
# a=1
# b=5
# print(a+b)

# Q2 Write a python program to find remainder when a no. is divided by z
# a=34
# b=5
# print("Remainder when a is divided by b is", a%b)

#Q3 Check the type of variable assigned using input() function.
# a= input("Enter the value of a:")
# print(type(a))

#Q4 Use comperision operater to find weather a given variable a is greater than 'b' or not. Take a=34 and b=80.
# a=int(input("Enter no. 1: "))
# b=int(input("Enter no. 2: "))
# print("a is grater than b is", a>b)

#Q5 Write a python program to find an average of two no. entered by the user.
# a=int(input("Enter no. 1: "))
# b=int(input("Enter no. 2: "))
# print("The average of two no is:", (a+b)/2)

#Q6 Write a python program to calculate the square of no. entered by the user.
# a=int(input("Enter a no."))
# print("The square of a no is:", a*a)

#Chapter 3 practice

#Q1 Write a python program to display a user entered of student followed by Good Afternoon using input() function.
# of student = input("Enter your of student: ")
# print(f"Good Afternoon, {of student}")

# Q2 Write a program to fill a letter template given below with of student and date.
# letter = '''Dear <|of student|>,
#          You are selected!
#          <|Date|>'''
# print(letter.replace("<|of student|>", "Uttam").replace("<|Date|>", "10 December 2002"))         

# Q3 Write a program to detect double space in string.
# of student = "Uttam is a good  boy."
# print(of student)
# print(of student.find("  "))

# Q4 Replace the double space from problem 3 with single spaces.
# of student = "Uttam is a good  boy."
# print(of student.replace("  "," "))

# Q5 Write a program to format the following letter using escape sequence characters.
# letter="Dear Uttam, this python course is nice. Thanks!"
# letter="Dear Uttam,\n\tThis python course is nice.\nThanks!"
# print(letter)

# Example
# String
# a="Uttam"
# a[0]="I"
# print(a[0])

# List
# friends=["Uttam", "Rohan", "Grapes", 43, 65.55, False]
# print(friends[0])
# friends[0]="Mango"
# print(friends[0])

# Tuple 
# a=int(1, 234, 4.67, "Uttam", False)
# print(type(a))

# Chapter 4 Practice

# Q1 Write a program to store seven fruits in a list entered by the user.'
# marks=[]
# f1=int(input("Enter marks of student:"))
# marks.append(f1)
# f2=int(input("Enter marks of student:"))
# marks.append(f2)
# f3=int(input("Enter marks of student:"))
# marks.append(f3)
# f4=int(input("Enter marks of student:"))
# marks.append(f4)
# f5=int(input("Enter marks of student:"))
# marks.append(f5)
# f6=int(input("Enter marks of student:"))
# marks.append(f6)
# f7=int(input("Enter marks of student:"))
# marks.append(f7)
# print(marks)

# Q2 Write a program to accept marks of six students to display them in a stored manner.
# marks=[]
# f1=int(input("Enter marks of student:"))
# marks.append(f1)
# f2=int(input("Enter marks of student:"))
# marks.append(f2)
# f3=int(input("Enter marks of student:"))
# marks.append(f3)
# f4=int(input("Enter marks of student:"))
# marks.append(f4)
# f5=int(input("Enter marks of student:"))
# marks.append(f5)
# f6=int(input("Enter marks of student:"))
# marks.append(f6)
# marks.sort()
# print(marks)

# Q3 Check that tuple type cannot be changed in python.
# a=(34, 342, "Uttam")
# a[2]="Larry"

# Q4 Write a program to sum a list with 4 numbers.
# a=[23, 34, 65, 123]
# print(sum(a))

# Q5 Write a program to count the number of zeros in the following tuple: 
# a=(7, 0, 8, 0, 0, 9)
# a=(7, 0, 8, 0, 0, 9)
# print(a.count(0))

# Chapter 5 practice

# Q1 Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# words={
#     "madad":"Help",
#     "kursi":"chair",
#     "billi":"cat"
# }
# word=input("Enter the word you want meaning of:")
# print(words[word])

# Q2 Write a program to input eight numbers from the user and display all the unique numbers(once).
# s=set()
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# num=input("Enter number : ")
# s.add(int(num))
# print(s)

# Q3 Can we have a set with 18(int) and '18'(str) as a value in it?
# s=set()
# s.add(18)
# s.add("18")
# print(s)

# Q4 What will be the length of following set s:
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))

# Q5 s={}. What is the type of 's'?
# s={}
# print(type(s))

# Q6 Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# dict={}
# name=input("Enter friends name: ")
# lang=input("Enter languge name: ")
# dict.update({name:lang})
# name=input("Enter friends name: ")
# lang=input("Enter languge name: ")
# dict.update({name:lang})
# name=input("Enter friends name: ")
# lang=input("Enter languge name: ")
# dict.update({name:lang})
# name=input("Enter friends name: ")
# lang=input("Enter languge name: ")
# dict.update({name:lang})
# print(dict)

# Q7 If the names of two friends are same; what will happen to the program in problem 6?
# It will update the dictonary. only the key will be update and the value will be same.

# Q8 If language of two friends are same; what will happen to the program in problem 6?
# Nothing will happen. The values can be same.

# Q9 Can you change the values inside a list which is contained in set is S?
# s={8,7,12,"Harry",[1,2]}
# No we can't

# Chapter 6 Practice

# Q1 Write a program to find the gratest of four numbers entered by the user.
# a=int(input("Enter a no.: "))
# b=int(input("Enter a no.: "))
# c=int(input("Enter a no.: "))
# d=int(input("Enter a no.: "))
# if(a>b and a>c and a>d):
#  print(a)
# elif(b>a and b>c and b>d):
#  print(b)
# elif(c>a and c>b and c>d):
#  print(c)
# elif(d>a and d>b and d>c):
#     print(d)

# Q2 Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.
# phy=int(input("Enter marks obtained: "))  
# che=int(input("Enter marks obtained: "))  
# bio=int(input("Enter marks obtained: "))  
# total_percentage=(100*(phy+che+bio))/300
# if(total_percentage>=40 and phy>=33 and che>=33 and bio>=33):
#     print("You are passed", total_percentage)
# else:
#     print("You are failed: ", total_percentage)
     
# Q3 A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "suscribe this", "click this". Write a program to detect these spams.
# p1="Make a lot of money"
# p2="buy now"
# p3="suscribe this"
# p4="click this"
# message=input("Enter your comment: ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("The comment is spam")
# else:
#     print("The comment is not spam")

# Q4 Write a program to find weather a given username contains less than 10 characters or not.
# a=input("Enter username: ")
# if(len(a)<10):
#     print("Username contains less than 10 characters")
# else:
#     print("Usename not contains less then 10 characters") 

# Q5 Write a program which finds out weather a given name is present in a list or not.
# l=["Uttam", "Divya", "Aditi", "Akash"]
# name=input("Enter your name: ")
# if(name in l):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

# Q6 Write a program to calculate the grade of the student from his marks from the following scheme:
# marks=int(input("Enter the mark of the student: "))
# if(marks<50):
#     print("Grade F")
# elif(marks>=50 and marks<=60):
#     print("Grade D")
# elif(marks>60 and marks<=70):
#     print("Grade C")
# elif(marks>70 and marks<=80):
#     print("Grade B")
# elif(marks>80 and marks<=90):
#     print("Grade A")
# elif(marks>90 and marks<=100):
#     print("Grade Ex")

# Q7 Write a program to find out weather a given post is talking about "Uttam" or not.
# post=input("Enter the post: ")
# if("Uttam".lower() in post.lower()):
#     print("Post is talking about uttam")
# else:
#     print("Post is not talking aboput uttam")

# Chapter 7
# a=1
# while(a<=50):
#     print(a)
#     a +=1

# Eg: Write a program to print the content of a list using while loops.
# l=[1, "Uttam", False, "This", "Harry"]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i +=1

# Chapter 7 Practice

# Q1 Write a program to print multiplication table of a given no. using for loop.
# a=int(input("Enter a no.: "))
# for i in range(1,11):
#     print(f"{a} X {i} = {a*i}")

# Q2 Write a program to greet all the person names stored in a list 'l' and which starts with s.
# l=["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# Q3 Attempt problem 1 using while loop.
# a=int(input("Enter a no.: "))
# i=1
# while(i<11):
#     print(f"{a} X {i} = {a*i}")
#     i +=1

# Q4 Write a program to find whether a given no. is prime or not.
# a=int(input("Enter a no.: "))
# for i in range(2,a):
#     if(a%i)==0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# Q5 Write a program to find the sum of first n natural numbers using while loop.
# n=int(input("Enter a no.: "))
# i=1
# sum=0
# while(i<=n):
#     sum +=i
#     i +=1
    
# print(sum)

# Q6 Write a program to calculate the factorial of a given number using for loop.
# n=int(input("Enter a no: "))
# product=1
# for i in range(1, n+1):
#     product=product*i
    
# print(product)    

''' Q7 Write a program to print the following star pattern.
  *
 ***
***** '''

# n =int( input("Enter a no: "))
# for i in range  (1, n+1):
#   print(" "* (n-i), end="")
#   print("*"* (2*i-1), end="")
#   print("")
  
'''Q8 Write a program toprint the following star pattern.
*
**
***
''' 
# n=int(input("Enter a no.: "))
# for i in range (1, n+1):
#   print("*"* (i), end="")
#   print("") 

'''Q9 Write a program to print the following star pattern.
***
* *
***
''' 
# n=int(input("Enter a no.: "))
# for i in range (1, n+1):
#   if(i==1 or i==n):
#     print("*"* n, end="")
#   else:
#     print("*" , end="")
#     print(" "* (n-2), end="")
#     print("*", end="")
#   print("")

'''
Q10 Write a program to print multiplication table of n using for loop in reversed order. 
'''
# n=int(input("Enter a no.: "))
# for i in range (1, 11):
#   print(f"{n} X {11-i} = {n*(11-i)}")

# Chapter 7

