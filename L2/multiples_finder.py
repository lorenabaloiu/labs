multiples = []
x = int(input("Enter a number: "))
limit = int(input("Enter a limit for your multiples: "))
for i in range(x,limit+1,x):
    multiples.append(i)
print("The number's multiples are: ",multiples)