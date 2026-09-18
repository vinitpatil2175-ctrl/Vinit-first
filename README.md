# Vinit-first
My Firsty Repository
Author - Vinit Patil




#For finding sum of first n natural no.s with recursion and def fun
def sum(n):
  if (n>=10 or n<=0):
    return 0
  else:
    return sum(n-1) + n
    
print(sum(5)) 
