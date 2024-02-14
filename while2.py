#find the favctors of a number using while loop
num=int(input("enter number to find its factor:"))
print(num,"factors are")
print(1,end=" ")
factor=2
while factor<=num/2:
    if num%factor==0:
        print(factor,end=" ")
    factor+=1
print(num,end=" ")
