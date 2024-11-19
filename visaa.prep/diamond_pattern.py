def print_diamond_pattern(N):
    for i in range(1,N+1):
        star='*'*i
        spaces=' '*(2*(N-i))
        print(star+spaces+star)
    for i in range(N-1,0,-1):
        star='*'*i
        spaces=' '*(2*(N-i))
        print(star+spaces+star)
N=int(input().strip())
print_diamond_pattern(N)
