name = "Amina"
age = 20
course = "PLP"
scores = [85, 90, 78]

average = sum(scores) / len(scores)

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Scores:", scores)
print("Average:", average)

if average >= 70:
    print("Result: Pass")
else:
    print("Result: Fail")