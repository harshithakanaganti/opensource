def can_achieve_marks(N, X, Y):
    if Y%X==0 and Y<=N*X:
        return "YES"
    return "NO"
N, X, Y=map(int, input().split())
print(can_achieve_marks(N, X, Y))
