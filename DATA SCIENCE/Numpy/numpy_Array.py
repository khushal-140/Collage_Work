import numpy as np
data=np.array([[10,20,30,40],
              [50,60,70,71]])
print(data)
print(data[0,1])#Row Columns
print(data[1,3])
print(data[0,0:3])
print(data[0,:])
print(data[1,1:3])
print(data[:,1:3])
print(data[1,1])
info=np.array([10,20,30,40,50,60,70])
#print(data.reshape(1,8))#Convert Two Dimestion to one Dimenstion(Dimision,column)
# flat=data.flatten() # Convert Two Dimestion to Two Dimenstion
# print(flat)
print(data.transpose())#Convert Row into Column and column into Row


#Add, Sub, Div,Mul, Squaer Root
add=np.add(info,500)

Mul=np.multiply(info,100)
sub=np.subtract(info,100)





div=np.divide(info,2)
squaroot=np.power(info,2)
print("Adddition",add)
print("Mulitiplication:",Mul)
print("Subration: ",sub)
print("Division:",div)
print("Square Root",squaroot)





