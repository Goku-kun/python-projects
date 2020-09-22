def GCD(a, b) :
    if (a>b):
        return GCD(a-b,b)
    elif (b>a):
        return GCD(a,b-a)
    else :
        return a
a = input("Enter the first number:\n")
b = input("Enter the second number:\n")
print("{} is the answer".format(GCD(int(a),int(b))))