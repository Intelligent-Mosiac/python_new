'''a=[1,4,2,6,7,3,5]

for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while j>=0 and a[j]>key:
        a[j+1]=a[j]
    a[j+1]=key
print(a)'''

"""fibonacci Numbers 
1,1,2,3,5,8,13,21,34,55"""
def fib(n):
   if n==0:return 0
   elif n==1:return 1
   else:return fib(n-1)+fib(n-2)
print(fib(6))




        