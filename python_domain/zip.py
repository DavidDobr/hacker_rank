N, X = map(int, input().split())
#print(N, X)

all_marks = [map(float, input().split()) for subject_j in range(X)]
students_marks = zip(*all_marks)

[print(sum(Si)/len(Si)) for Si in students_marks]
