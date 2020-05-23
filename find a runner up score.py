if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=sorted(arr)
    b=max(a)
    while max(a) == b:
        a.remove(max(a))
    print(max(a))