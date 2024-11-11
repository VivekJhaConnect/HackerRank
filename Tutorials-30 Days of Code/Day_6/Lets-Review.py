# Enter your code here. Read input from STDIN. Print output to STDOUT
input_number = int(input())
input_str = []

for i in range(0, input_number):
    inp = str(input())
    odd = []
    even = []
    for j in range(0, len(inp)):
        if j == 0:
            odd.append(inp[j])
        elif j == 1:
            even.append(inp[j])
        elif j % 2 == 0:
            odd.append(inp[j])
        else:
            even.append(inp[j])
        
    print(f"{''.join(odd)} {''.join(even)}")
    odd = []
    even = []
    
