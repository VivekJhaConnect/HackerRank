if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if len(arr)==1:
        print(arr[0]) 
    first_high = arr[0]
    for i in arr:
        if first_high > i:
            print(i)
            break