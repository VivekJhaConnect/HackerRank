'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    student_score = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_score[name] = score
    
    second_min = 0
    arr = list(student_score.values())
    
    arr.sort()
    if len(arr)==1:
        second_min = arr[0] 
    first_min = arr[0]
    for i in arr:
        if first_min < i:
            second_min = i
            break
    
    result = []
    for key in student_score.keys():
        if student_score[key] == second_min:
            result.append(key)
    result.sort()
    for val in result:
        print(val) 