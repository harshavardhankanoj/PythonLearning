if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    tem=arr[::-1]
    for i in tem:
        print(i,end=" ")