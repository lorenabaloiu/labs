x = input("Enter a number: ")
x = int(x)
k = int(x/2)
if x%2==0 | x==1:
    print ("This is not a prime number!")
else:
    for i in range(1, k):
        if x%i==0:
            ok=1
        else:
            ok=0
    if ok==1:
        print("This number is not a prime number!")
    else:
        print("This number is a prime number!")