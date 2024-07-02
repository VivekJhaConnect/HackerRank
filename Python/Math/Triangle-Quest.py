'''
You are given a positive integer . Print a numerical triangle of height like the one below:

1
22
333
4444
55555
......
'''
for i in range(1, int(input())):
    print(sum(map(lambda x: i * (10**x), list(range(i)))))