def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i]>=38 and (grades[i]%5==3 or grades[i]%5==4):
            grades[i]=grades[i]+(5-grades[i]%5) 
    return grades  Q