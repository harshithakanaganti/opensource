n=int(input())
k=int(input())
m=1<<(k-1)
if n&m:
    print("true")
else:
    print("false")
