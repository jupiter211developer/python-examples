L1 = ["John", 102, "USA"]    
L2 = [1, 2, 3, 4, 5, 6]   

print(type(L1))  
print(type(L2))  

T1 = (101, "Peter", 22)    
T2 = ("Apple", "Banana", "Orange")     
T3 = 10,20,30,40,50  
  
print(type(T1))  
print(type(T2))  
print(type(T3))  

tuple1 = tuple(input("Enter the tuple elements ..."))  
print(tuple1)    
count = 0    
for i in tuple1:    
    print("tuple1[%d] = %s"%(count, i))   
    count = count+1  

tuple = (1,2,3,4,5,6,7)  
#element 1 to end  
print(tuple[1:])  
#element 0 to 3 element   
print(tuple[:4])  
#element 1 to 4 element  
print(tuple[1:5])   
# element 0 to 6 and take step of 2  
print(tuple[0:6:2])  