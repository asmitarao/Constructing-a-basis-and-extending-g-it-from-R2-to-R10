import math
import copy
import time
print('Enter the number of vectors in the matrix') 
k = int(input()) 
d=2
u = []
# taking the input of the array  
v=[[[] for i in range(k)] for i in range(2)]
for i in range(k):
  for j in range(k):
     number=int(input("Enter Elements of Matrix :")) 
     v[i][j]=number
  
def multiply(x=[],y=[]): # each element of the list is being multiplied
  result = 0
  for i in range(d):
     result += x[i] * y[i]
  return result

def multiply1(x=[],y=[]): # each element of the list is being multiplied and sqaure root is taken
  result = 0
  for i in range(d):
     result += x[i] * y[i]
  result = math.sqrt(result)
  return result
  
def subtract(x,y): #function used to subtract two lists
 for i in range(d):
     x[i]=x[i]-y[i]
 return x

def main():
	res=multiply1(v[0],v[0]) # v is the nested list,  passing only the first list to function
	try:
		u[0] = []
	except:
		u.append([])
	for j in range(d):
		u[0].append(v[0][j]/res)
	for i in range(1,k): 
		v1=[]
		try:
			u[i] = []
		except:
			u.append([])  
		for l in v[i]:
			u[i].append(l) #u[i] gets value in v[i]
		z=0
		for j in range(0,i):
			ans=multiply(v[i],u[j])
			cpy=[]
			cpy=list(map(lambda x: ans*x, u[j]))
			u[i] = subtract(u[i],cpy) 
            
		product=multiply1(u[i],u[i]) #norm is calculated
		if(product!=0):
			for m in range(d):
				u[i][m]=u[i][m]/product
		

a=[0,0,4]
for i in range(9): #for loop to extend the dimensions of the array
	startTime = time.time()
	main()
	elapsedTime = time.time() - startTime
	print(elapsedTime)
	print("----------------")
	for row in v:
		row.append(0)
	v.append([])
	for i in a:
		v[-1].append(i)
	d=d+1
	k=k+1
	a.insert(0, 0)
print(u)
