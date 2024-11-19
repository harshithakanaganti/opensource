def high_altitude(n,heights):
    curr_altitude=0
    max_altitude=0
    for height in heights:
        curr_altitude+=height
        max_altitude=max(max_altitude,curr_altitude)
    return max_altitude
n=int(input().strip())
heights=list(map(int, input().strip().split()))
print(high_altitude(n, heights))
