def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n=5
if n<0:
    print("sorry fact does not exist negative memers")
else:
    print("the fact of",n,"is",fact(n))
