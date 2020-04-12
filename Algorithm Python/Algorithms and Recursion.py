a=[8,4,1,3,2,6]
count=0
# Bubble Sort
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j-1] > a[j]:
            count+=1
            a[j-1],a[j]=a[j],a[j-1]# Swapping of 2 variable 1 linear
print(a,count)
#Insertion Sort   
a=[6,5,3,1,8,7,2,4]
count=0
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    
    while j>=0 and a[j]> key:
        a[j+1]=a[j]
        count+=1
        j-=1
    a[j+1]=key
print(a,count)   

#Factorials using Recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(6))

# Binary Search through Recursion
a=[1,5,7,8,11,13,16]
def binary_search(a,key,start,end):
    if start<=end:
        mid=int((start+end)/2)
        if a[mid]>key:
            return binary_search(a,key,start,mid-1)
        elif a[mid]<key:
            return binary_search(a,key,mid+1,end)
        else:
            return mid
    print(key,"Could not be found")
    return -1
print(binary_search,(a,5,0,len(a)-1))

#fibonacci Series Using Recursion(H.W)



