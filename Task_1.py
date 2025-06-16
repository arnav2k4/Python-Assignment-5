stuMarks = {'A': 50, 'B': 40, 'C': 60}
stu = input("Enter student name: ")
if stu in stuMarks:
    print("{}'s marks: {}.".format(stu, stuMarks[stu]))
else:
    print("{} not found.".format(stu))
