#for else
#if there is any break in for loop, the else block is not excuted
numbers=[1,2,3,4,0,6,7,8,89]
for i in numbers:
    print(i)
    if i==0:
        break
else:
    print("successfully completed")
