def fibonacci(n):

    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
n=int(input("enter num : "))
fibonacci(n)
# # Program to display the Fibonacci sequence up to nth term

# # Input: number of terms
# n = int(input("Enter the number of terms: "))

# # Initialize the first two terms
# a, b = 0, 1

# # Check if the number of terms is valid
# if n <= 0:
#     print("Please enter a positive integer.")
# elif n == 1:
#     print("Fibonacci sequence up to", n, "term:")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     for i in range(n):
#         print(a, end=" ")
#         # Update values for next terms
#         a, b = b, a + b
