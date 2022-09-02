def main():
    seq = [int(i) for i in input().split()]
    r = False
    n = len(seq)

    for i in range(n):
        if (crescente(seq[i:]+seq[:1])):
            r = True
            break

def crescente(v):
    i = 0
    while(i<len(v)- 1):
        if(v[i]>v[i+1]):
            return False
        i = i + 1
    return True
main()