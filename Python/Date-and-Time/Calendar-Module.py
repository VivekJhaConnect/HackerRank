# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

date_str = input()
date_obj = datetime.datetime.strptime(date_str, '%m %d %Y')

day_name = date_obj.strftime('%A')

print(day_name.strip().upper())