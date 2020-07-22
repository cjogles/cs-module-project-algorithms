'''
Input: an integer
Returns: an integer
'''

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))



# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 6

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
