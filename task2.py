import pandas as pd

def get_letter_grade(score):
    if 90 <= score <= 100:
         grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade
def get_GPA(x):
    if x == 'A':
        return 4.0
    if x == "B":
        return 3.0
    if x == "C":
        return 2.0
    if x == "D":
        return 1.0
    if x == "F":
        return 0.0    

FILENAME = 'scores.csv'
df_scores = pd.read_csv(FILENAME, delimiter = ',', index_col=0,header=0)

df_letter_grades = df_scores.applymap(get_letter_grade)
df_GPA_point = df_letter_grades.applymap(get_GPA)

df_GPA_point['The class GPA is'] = df_GPA_point.mean(axis=1)
df_GPA_point = df_GPA_point.transpose()
df_GPA_point['GPA'] = df_GPA_point.mean(axis=1).round(2)

series = df_GPA_point['GPA']
print(series.to_string())



