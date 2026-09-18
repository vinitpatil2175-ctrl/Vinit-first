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

#recusive function to print all ele of list
def print_list(list,idx=0):
  if(idx>=len(list)):
    return
    print(list,idx)
    print_list(list,idx+1)

fruits = ["apple","orange"]
print_list(fruits)



