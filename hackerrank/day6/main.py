T = int(input())
for _ in range(T):
    s = input().strip()
    pares = s[::2]
    impares = s[1::2]
    print(pares, impares)