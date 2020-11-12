"""Lab activity Strings """
#Question 1 of Lab Activity 
def f1():
    n=input("Enter your number")
    num=65

    for i in range(0,n):

        if i==0:

            for j in range(0,n):

                print(chr(num+j),end=' ')
            for j in range(n-2,-1,-1):

                print(chr(num+j),end=' ')

        else:

            for j in range(0,n-i):

                print(chr(num+j), end='  ')

            for j in range 
    
