import math
X,N=map(int, input().split())
capacity=X*100
if N<=capacity:
    print(0)
else:
    extra_pass=N-capacity
    planes_needed=math.ceil(extra_pass/100)
    print(planes_needed)
