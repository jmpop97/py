import time
a=[1,2,3,4,5]
dics={3:"공민영",2: "박혜린" ,5: "최준영" ,1: "김정은" ,4:"박종민"}

def changes(x,a,b):
    x1=x[:]
    x1[a]=x[b]
    x1[b]=x[a]
    return x1
    

def change5(x):
    n=(x[4])%5 +1
    m=x.index(n)
    x1=changes(x,m,4)
    return x1

while True:
    
    print_a=[]

    for ele in a:
        print_a.append(dics[ele])
    print(print_a)
    a=changes(a,3,0)
    a=changes(a,1,2)
    a=change5(a)


    
    if a==[1,2,3,4,5]:
        break

