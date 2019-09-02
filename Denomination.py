#!/usr/bin/env python
# coding: utf-8

# In[10]:


n=int(input("the amount of money:"))
a=0
b=0                 #a,b,c,d,e,f,g denote 2000,500,200,100,50,20,10 rupees
c=0
d=0
e=0
f=0
g=0
h=0

while(n>=2000):
    y=n-2000
    a+=1
    n=y
while(n>=500):
    y=n-500
    b+=1
    n=y
while(n>=200):
    y=n-200
    c+=1
    n=y
while(n>=100):
    y=n-100
    d+=1
    n=y
while(n>=50):
    y=n-50
    e+=1
    n=y
while(n>=20):
    y=n-20
    f+=1
    n=y
while(n>=10):
    y=n-10
    g+=1
    n=y
    
while(n>=1):
    y=n-1
    h+=1
    n=y
    
print("Rs.2000=" ,a,"Rs.500=" ,b,"Rs.200=" ,c,"Rs.100=" ,d,"Rs.50=" ,e,"Rs.20=" ,f,"Rs.10=" ,g,"Rs.1=" ,h)
    

    


# In[ ]:





# In[ ]:




