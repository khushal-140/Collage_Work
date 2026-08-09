import numpy as np
array=np.array([70,80,90])
print(array)  #One Dimension Array 
matix=np.array([[70,80,90],
                [78,79,80],
                [80,81,82]])
print(matix)    #Two Dimension Array 

array_defalut=np.zeros((2,3),dtype=int)
array_defalut[0][0]=1
print(array_defalut) #defalut matxi

array_defalut_string=np.full((2,3),"P",dtype=str)
print(array_defalut_string) #defalut martxi with String

arrange=np.arange(1,6) #(start,stop,step)
print(arrange) #range like function Array

linspace=np.linspace(60,100,5,dtype=int) #(start, stop , gap)
print(linspace) #fiind gap and return the value 

randrom=np.random.randint(1,100,5) #(start,stop,number want) 
print(randrom) #Give random Number