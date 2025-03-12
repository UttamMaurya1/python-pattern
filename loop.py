''' For loop '''

'''Fabonacci series '''
# n=int(input("Enter a number: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range (3,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)

''' factorial '''
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

''''''
n = int(input("Enter a no: "))
result = 1
computations = []

# Compute factorial steps and store results
for i in range(1, n + 1):
    result *= i
    factors = [f"{n}"] + [f"{j}" for j in range(i, 0, -1)]
    computations.append((" * ".join(factors), result))

# Print in ascending order
for factors, value in computations:
    print(f"{factors} = {value}")

print()  # Just for spacing

# Print in descending order
for factors, value in reversed(computations):
    print(f"{factors}={value}")