def average(array):
    # your code goes here
    set_list = set(array)
    return "{:.3f}".format(sum(set_list)/len(set_list))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)