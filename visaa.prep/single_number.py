def find_single_number(arr):
    res=0
    for num in arr:
        res^=num
    return res
n=int(input().strip())
arr=list(map(int, input().strip().split()))
print(find_single_number(arr))
