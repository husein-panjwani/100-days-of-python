student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grade = {}


for i in student_scores:
    score = student_scores[i]
    if score >90:
        student_grade[i] = "Outstanding"
    elif score >80 :
        student_grade[i] = "Exceeds Expectations"
    elif score >    70:
        student_grade[i] = "acceptable"
    elif score < 70:
        student_grade [i] = "fail"

print (student_grade)