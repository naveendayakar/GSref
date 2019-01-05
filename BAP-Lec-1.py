import numpy as np
import pandas as pd

vv=[1,8,2,4,5,8,0,2]
def prob1(w):
    big_w=w[0]
    big_i=0
    new_w=[]
    for i in range(len(w)-1):
        if big_w<w[i+1]:
            big_i=i+1
            big_w=w[i+1]
    new_w.append(big_w)
    for z in w:
        if z!=big_w:
            new_w=new_w+[z]
    return sum(new_w)
o=prob1(vv)

o



vv = [4,1,5,3,8,8]
def prob2(v):
    big_v=v[0]
    big_i=0
    for i in range(len(v)-1):
        if big_v<v[i+1]:
            big_i=i+1
            big_v=v[i+1]
    del v[big_i]
    m = int(len(v)/2)
    new_v=[]
    for i in range(m):
        new_v.append(v[i])
    new_v.append(big_v)
    for i in range(m,len(v)):
        new_v.append(v[i])
    return sum(new_v[2:len(new_v)])

a=prob2(vv)
b=prob2(vv)

a
b



mm = np.array([[3,2,1],[1,5,4],[2,6,7]])
def prob3(m):
    m2 = m.copy()
    a = m[:,0].max()
    x,y = m.shape
    for i in np.arange(x):
        b = m[:,0].argmin()
        m2[i,:]=m[b,:]
        m[b,0]=a+1
    return m2
mm2 = prob3(mm)
mm2





mm = np.array([[3,2,1],[1,5,4],[2,6,7]])
def prob3(m):
    m2 = m
    a = m[:,0].max()
    x,y = m.shape
    for i in np.arange(x):
        b = m[:,0].argmin()
        m2[i,:]=m[b,:]
        m[b,0]=a+1
    return m2
mm2 = prob3(mm)

mm2



mm = np.array([[8,0,3],[8,7,8],[2,1,0]])
def prob5(m):
    m_max = m.max()
    x,y = m.shape
    m2 = m.flatten()
    i = 0
    c = len(m2)-1
    while i==0:
        if(m2[c]==m_max):
            i = 1
            m2[c]=m_max-3ad
        else:
            c = c - 1
    return m2.reshape(x,y)
mm2 = prob5(mm)


mm2



mm = np.array([[6,8,5,5,3,2,6,7,8,8,8,7,3,2,5,7],
[1,6,7,3,8,8,4,7,6,7,5,8,3,4,8,8],
[2,3,1,4,2,2,0,8,3,5,8,8,7,7,3,4]])
def prob6(m):
   x = m
   x[:,[1,3,5,7,9,11,13,15]]=x[:,[0,2,4,6,8,10,12,14]]*2
   w = x - 9
   x[x>9]=v[x>9]
   v =x.sum(axis=1)
   res = np.array(['justin']*3)
   res[v%10==0]='selena'
   return res
mm2=prob6(mm)

mm2






o1 = np.array([[1,5,6],[7,8,2]])
o2 = np.array([[3,4],[10,6],[5,7]])
r1,c1 = o1.shape
r2,c2 = o2.shape
a1=o1.flatten()
a2=o2.flatten()
o3=np.concatenate((a1, a2))
o4 = np.sort(o3)
s=r1 * c2
r = len(o4)-s
r = int(r/2)
o5=np.shape(o4)
o5.reshape(r1,c2)

def prob7(o1,o2):
    r1,c1 = o1.shape
    r2,c2 = o2.shape
    a1 = o1.flatten()
    a2 = o2.flatten()
    o3 = np.concatenate((a1, a2))
    o4 = np.sort(o3)
    s=r1 * c2
    r = len(o4)-s
    r = int(r/2)
    o5=np.shape(o4)

    return o5.reshape(r1,c2)
    
prob7(o1,o2)




def prob8(v):
    v2 = str(v)
    while len(v2)>1:
        tot = 1
        for i in v2:
            
            
#      (missing)      
#      (missing)      
#      (missing)
        v2 = str(tot)
    return int(v2)
prob8(5503467)
#Ans 2


r = M.sum(axis=1)
r
index=r.argmax(axis=0)
index


#9) Fill in the missing code.  The function below finds the sum of the row, that has the largest difference from N.

Z = [[1,3,6],[2,7,1],[5,2,8]]
M = np.array(Z)
N = 4
M

def prob9(M,N):
    r = M.sum(axis=1)
    index=r.argmax(axis=0)
    return M[index]
    
prob9(M,N)
#array([5, 2, 8])

#10) What are the values for bb[0]?   
JJ=[5,2,9,1,8,7]

def prob10(n,j):
    jj = np.array([j])
    new_v=[]
    new_v=np.append(new_v,jj[jj>n])
    n=n+8
    new_v2=[]
    new_v2=np.append(new_v2,new_v[new_v<n])
    return new_v

bb = prob10(7,JJ)


bb[0]




#11) What is c[3]?    
vv=np.array([12,11,14,15,13])
a=np.array([12,14,14,12,14])

vv[0:5]
a[0:5]


c=[]
c = np.append(c,vv[0:5]+a[0:5])
c = np.append(c,vv[4:len(vv)]*a[4:len(a)])
c[3]







