def print_star_pattern(N):
    for i in range(1,N+1):
        print('*'*i)
    for i in range(N-1,0,-1):
        print('*'*i)
N=int(input().strip())
print_star_pattern(N)
