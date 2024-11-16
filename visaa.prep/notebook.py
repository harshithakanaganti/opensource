def calc_note(N):
    total_pg=N*1000
    notebooks=total_pg//100
    return notebooks
N=int(input().strip())
result=calc_note(N)
print(result)
