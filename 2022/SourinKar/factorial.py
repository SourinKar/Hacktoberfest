n=int(input("enter no."))
factorial=1
if n==0:
  print("factorial of 0 is 1")
else:
  while (n>0):
    factorial=factorial*n
    n=n-1
    
print("factorial of given no. is:", factorial)
