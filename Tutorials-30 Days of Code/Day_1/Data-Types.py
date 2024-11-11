i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

int_val: int = 0
double_val: float = 0.0
str_val: str = ''
# Read and save an integer, double, and String to your variables.
int_val = int(input())
double_val = float(input())
str_val = str(input())

# Print the sum of both integer variables on a new line.
print(str(i+int_val))

# Print the sum of the double variables on a new line.
print(str(d+double_val))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(f"{s}{str_val}")
