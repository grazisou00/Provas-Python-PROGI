def is_M_alternate(n, seq):
    if n <= 1:
        return False
    m = 1
    for i in range(1, n):
        if (seq[i] % 2 == 0) == (seq[i-1] % 2 == 0):
            return False
        m = max(m, i+1)
    return m

while True:
    n = int(input("Informe n: ").strip())
    if n == 0:
        break
    seq = list(map(int, input("Informe a sequencia: ").strip().split()))
    m = is_M_alternate(n, seq)
    if m:
        print(m)
    else:
        print("NAO")
    print("%")
