a=[8,4,1,3,2,6]
count=0
# Bubble Sort
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j-1] > a[j]:
            count+=1
            a[j-1],a[j]=a[j],a[j-1]# Swapping of 2 variable 1 liner
print(a,count)
#Insertion Sort   
a=[6,5,3,1,8,7,2,4]

for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]> key:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)    


