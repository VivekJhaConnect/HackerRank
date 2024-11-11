size = int(input())
numbers = list(map(int, input().split()))

# Calculate mean
mean = sum(numbers) / len(numbers)
print(mean)

# Calculate median
numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]
print(median)

# Calculate mode
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_freq = max(frequency.values())
modes = [k for k, v in frequency.items() if v == max_freq]
mode = min(modes)
print(mode)