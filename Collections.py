#list 

fruits  = [ "apple",  "banana",  "cherry", "mango"] 


print(fruits) 

print(fruits[0])
print(fruits[-1])
print(fruits[-2])


fruits.reverse()
print(fruits)

fruits.append("jack") 

print(fruits)

fruits.remove("jack")

print(fruits)

fruits.sort()

print(fruits)

fruits.pop()

print(fruits)



#tupples 



point  = 10,  20 
days =  ("mon","tue",  "wed", "thu" , "fri",  "sat", "sun") 

print(point)

print(point[0])
print(days[2]) 

dictionaries 


isstudent = {
    'name': 'kamble' ,
    'age' : 22, 
    'grade' : "A"
 }


print(isstudent) 

print(isstudent['name']) 
print(isstudent.get('age')) 


isstudent['city'] = 'mumbai' 

print(isstudent)

del isstudent['city']

print(isstudent)


for key in  isstudent:
    print(key)