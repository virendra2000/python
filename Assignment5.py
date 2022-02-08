list1 = list(range(1,100))
  
r3 = list(filter(lambda x: (x % 3 == 0), list1)) 
r5 = list(filter(lambda x: (x % 5 == 0), list1)) 
  
print(r3,"These numbers are only divisible by 3 between 1-100 number \n") 
print(r5,"These numbers are only divisible by 5 between 1-100 number ")
