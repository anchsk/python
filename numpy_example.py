import numpy as np

# NumPy - numerical python
print(np.__version__) # 2.2.3

a = np.array([0,1,2,3,4])
print(a.size) 
print(a.ndim) # number of dimensions
print(a.shape) # size in each dimension

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b)) # <class 'numpy.ndarray'>
print(b.dtype) # float64

b[3:5]=200,499
print(b) # [  3.1   11.02   6.2  200.   499.  ]

# Vector addition and subtraction
u = np.array([1,0])
v = np.array([0,1])

z = u+v
print(z, type(z)) # [1 1] <class 'numpy.ndarray'>


u = [1,0]
v = [0,1]
z = []

for n,m in zip(u,v): 
    z.append(n+m)
    
print(z, print(type(z))) # [1, 1] None 


# Vector multiplication
y = np.array([1,2])
z = 2*y
print(z)

y = [1,2]
z = []
for n in y:
    z.append(2*y)
    
# Dot product (how similar the 2 vectors are)

# Universal functions

print(a.mean(), a.max())

np.pi

np.linspace(-2, 2, num = 5)
# 5 numbers distributed from -2 to 2

X=np.array([[1,0],[0,1]])

Y=np.array([[2,2],[2,2]]) 

Z=np.dot(X,Y) 
print('Z',Z)

a=np.array([0,1]) 
b=np.array([1,0]) 

np.dot(a,b) 

print('dot', np.dot(a,b))

a=np.array([0,1,0,1,0]) 

b=np.array([1,0,1,0,1]) 

arr = [0,23,1,12,7]
print(sorted(arr))

for i in range(1,5):
    if (i != 1):
        print(i)
        
def add(x):
    return x+x 
    # return(x+x) what's the difference?

print('1:2,3:4'.split(':'))

a = tuple([1,0,2])
print(a[2])
print(1/2, 1//2)
name = 'ABCDE'
print(name.find('B'))