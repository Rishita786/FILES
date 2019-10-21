#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def printResult(Distance,Path):
    print("Path :: ",end="")
    for x in Path:
        print("->",x,end="")
    print("\nDistance ::",Distance) 


# In[3]:


def GreedyPath(NodeCostMatrix,Source,Dest,node):
    Tour=[]
    TotalDistance=[]
    visited = [False for i in range(node)]
    visited[Source]=True
    Tour.append(Source)
    for j in range(node-1):
        minD=999
        for i in range(node):
            if visited[i] == False and i!=Tour[-1]: # checking for i : i is not visited and is not a source city
                if minD>NodeCostMatrix[Tour[-1],i]: # choosing minimum distance from last visited city 
                    minD=NodeCostMatrix[Tour[-1],i]
                    nextNode=i
        visited[nextNode]=True
        TotalDistance.append(minD)
        Tour.append(nextNode)
    #TotalDistance += NodeCostMatrix[Tour[-1],Source] #adding the distace b/w last city and source city
    #Tour.append(Source)
    ind=Tour.index(Dest)
    #print("ind :",ind)
    tour=Tour[0:ind+1]
    #print("tour :",tour)
    #print(Tour)
    tds=sum(TotalDistance[0:ind])
    return tds, tour


# In[5]:


CostMatrix = np.random.randint(1,10,(20,20))


# In[11]:


print("Enter coordinates :: ")
x,y = map(int,input().split())
l,m = map(int,input().split())
SubMatrix = CostMatrix[x:l,y:m]
print(SubMatrix)


# In[15]:


SubMatrix = CostMatrix[x:l,y:m]
leng=SubMatrix.shape
row=leng[0]
column=leng[1]
sou = 0
dest = row-1
cost1=cost2=0
#column will expand i.e l and m (assumning l will be less then or equal to m)
if row>column:
    ex=row-column
    if y-ex>=0:
        c1=CostMatrix[x:l,y-ex:m]
        print("Matrix 1 :\n",c1)
        cost1,path1=GreedyPath(c1,sou,dest,c1.shape[0])
    if m+ex!=20:
        c2=CostMatrix[x:l,y:m+ex]
        print("Matrix 2 : \n",c2)
        cost2,path2=GreedyPath(c2,sou,dest,c2.shape[0])
elif row<column:
    ex=column-row
    if x-ex>=0:
        c1=CostMatrix[x-ex:l,y:m]
        s1=0+ex
        d1=dest+ex
        print("Matrix 1 :\n",c1)
        cost1,path1=GreedyPath(c1,s1,d1,c1.shape[0])
    if l+ex!=20:
        c2=CostMatrix[x:l+ex,y:m]
        print("Matrix 2 : \n",c2)
        cost2,path2=GreedyPath(c2,sou,dest,c2.shape[0])
else:
    cost1,path1=GreedyPath(SubMatrix,sou,dest,row)
if cost1!=0 and cost2!=0:
    if cost1<cost2:
        printResult(cost1,path1)
    else:
        printResult(cost2,path2)
else:
    if cost1!=0:
        printResult(cost1,path1)
    elif cost2!=0:
        printResult(cost2,path2)


# In[ ]:


""""Sample:
    Input 
    Enter coordinates :: 
    2 9
    6 10
    [[9]
     [7]
     [4]
     [5]]
    Output
    Matrix 1 :
     [[4 4 6 9]
     [1 5 1 7]
     [6 5 8 4]
     [9 9 3 5]]
    Matrix 2 : 
     [[9 8 5 9]
     [7 4 2 2]
     [4 3 6 2]
     [5 6 6 2]]
    Path :: -> 0-> 2-> 3
    Distance :: 7""""
    

