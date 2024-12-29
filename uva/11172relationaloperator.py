n = int(input())
for line_num in range(n):
    a, b = map(int, input().split())
    if a == b: print("=")
    elif a > b: print(">")
    else: print("<")
