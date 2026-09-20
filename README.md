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


#recursive function to find a world in any of our textfiles
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()

    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")


#to remove any textfile from our system we can use the os module and its remove() method.
import os
os.remove ("practice.txt")


#For replacing some old data from file to new data
with open ("Pract.txt","r") as f:
    data = f.read()

    new_data = data.replace("Old data","New data")
    print(new_data)
        

