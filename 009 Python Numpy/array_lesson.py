from traceback import print_tb
import numpy as np

#Numpy array has a homogenous data type
# array_a=np.array([1,2,3,4,5])
# # print(array_a.shape)
# array_b=np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print(array_b.shape)

#3x3

# seq_a=[1,2]
# seq_b=[4,5]
# sec_c=[7,8]
# seq_d=[10,11]
# seq_e=[13,14]
# array_abc=np.array([seq_a,seq_b,sec_c,seq_d])
# # print(array_abc.shape)


# #assignment 5x2
# array_d=np.array([seq_a,seq_b,sec_c,seq_d,seq_e])
# # print(array_d.shape)

# Reshaping & Indexing NumPy Array
# array_a=np.array([[1,2,3],[4,5,6]], dtype=float)
# print(array_a)
# # print(array_a.size)

# # array_b=array_a.T
# # # print(array_b)
# # print(array_b[0])
# # print(array_b[:,1])
# # print(array_b[0,0])

# array_b=np.zeros((3,3))
# print(array_b)

# array_c=np.ones((3,3))
# print(array_c)
# array_d=np.full((3,3,),5)
# print(array_d)
# array_e=np.random.random((3,4))
# print(array_e)

row_1= [1,2,3,4,5]
row_2= [6,7,8,9,10]
row_3= [11,12,13,14,15]
row_4= [16,17,18,19,20]
row_5= [21,22,23,24,25]

test_data=np.array([row_1,row_2,row_3,row_4,row_5])
print(test_data)

#slice
print(test_data[:,2:4:1]) #start:ending value:stepsize
#negative index
print(test_data[:,-2:-4:-1])

#boolean 
greater_than_five=test_data> 5
print(greater_than_five)
print(test_data[greater_than_five])

#where
drop_under_5_array = np.where(test_data>5, test_data,0)
print(drop_under_5_array)

#logical and
drop_under_5_and_over_20=np.logical_and(test_data>5, test_data<20)
print(drop_under_5_and_over_20)
print(test_data[drop_under_5_and_over_20])