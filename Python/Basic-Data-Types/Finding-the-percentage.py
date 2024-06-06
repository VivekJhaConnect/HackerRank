if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks_list = student_marks[query_name]
    
    avg = sum(marks_list)/len(marks_list)
    print(format(avg, ".2f"))
